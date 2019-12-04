import html5lib
from html5lib.serializer import SerializeError
from nltk.tokenize import sent_tokenize

INLINE_ELEMENTS = {'a', 'abbr', 'acronym', 'b', 'bdi', 'bdo', 'big', 'cite', 'code', 'dfn', 'em', 'i', 'kbd',
                   'label', 'mark', 'nav', 'output', 'progress', 'q', 's', 'slot', 'small', 'span', 'strong',
                   'sub', 'sup', 'time', 'tt', 'var', 'wbr'}

# does not include pre or textarea (which are accounted for in PRESERVE_WHITESPACE_ELEMENTS
BLOCK_LEVEL_ELEMENTS = {'address', 'article', 'blockquote', 'caption', 'details', 'dialog', 'div', 'dl',
                        'dt', 'figcaption', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hgroup',
                        'li', 'main', 'ol', 'p', 'ul', 'section', 'table', 'tbody', 'td', 'th', 'thead', 'tr'}

HEADER_ELEMENTS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hgroup'}

SKIPPED_ELEMENTS = ["br", "hr"]

# elements which cannot contain children and denote the end of a sentence
EMPTY_ELEMENTS = {'area', 'base', 'br', 'embed', 'hr', 'img'}

# elements which can have children which never qualify as a sentence
SENTENCE_VOID_ELEMENTS = {'button', 'caption', 'col', 'colgroup', 'pre', 'table', 'textarea', 'td', 'tfoot',
                          'th', 'thead', 'tr'}


class InvalidTagError(Exception):
    def __init__(self, tag_name):
        super(InvalidTagError, self).__init__("Parsing an empty tag which is not of the accepted element types. It is "
                                              "of type {}".format(tag_name))


class HTMLSentenceTokenizer:

    def __init__(self, ignore_headers=True, raise_invalid_tags=False):
        """
        :param ignore_headers: If true, ignores text inside of the tags included in HEADER_ELEMENTS. This defaults to
        true because the text inside of these "header elements" is typically not a sentence.
        :param raise_invalid_tags: If true, raises an InvalidTagError when parsing a tag not in INLINE_ELEMENTS,
        BLOCK_LEVEL_ELEMENTS (which includes the elements of HEADER_ELEMENTS), SKIPPED_ELEMENTS, EMPTY_ELEMENTS, or
        SENTENCE_VOID_ELEMENTS. If false, ignores this tag and all of its children. (Sentences descending from it will
        not be included in the value returned from feed)
        """
        # self.parser is an etree parser by default.
        self.parser = html5lib.HTMLParser()
        self.walker = html5lib.getTreeWalker("etree")
        self.sentences = []
        self.ignore_header_text = ignore_headers
        self.raise_invalid_tags = raise_invalid_tags
        self.reset()

    def feed(self, markup):
        """
        Given an HTML document which contains tags on only INLINE_ELEMENTS, BLOCK_LEVEL_ELEMENTS, or
        PRESERVE_WHITESPACE_ELEMENTS, parses the HTML document into a BeautifulSoup-like tree represented by Node
        and TextNode objects. Stores these objects in the database. At the end, also resets this SentenceParser object
        by calling the reset() method.

        :return: The root node of the parsed tree.
        """
        etree_document = self.parser.parse(markup)
        stream = self.walker(etree_document)

        # todo: find a more efficient way to only iterate over tags that are a descendant of body
        passed_body = False

        for i in stream:
            if passed_body:
                if i['type'] == 'StartTag':
                    self.handle_starttag(i['name'])
                elif i['type'] == 'EndTag':
                    if i['name'] == 'body':
                        break
                    self.handle_endtag(i['name'])
                elif i['type'] == 'EmptyTag':
                    self.handle_empty_tag(i['name'])
                elif i['type'] == 'Characters' or (i['type'] == 'SpaceCharacters' and self.ignored_parent_count > 0):
                    self.handle_text(i['data'])
                elif i['type'] == 'SpaceCharacters':
                    self.handle_text(' ')
                elif i['type'] == 'SerializeError':
                    raise SerializeError(i['data'])
                # else, is a comment, doctype, entity, or unknown.
                else:
                    pass
            elif i['type'] == 'StartTag' and i['name'] == 'body':
                passed_body = True

        sentences_copy = self.sentences
        self.reset()
        return sentences_copy

    def reset(self):
        self.sentences = []
        self.ignored_parent_count = 0
        self.current_string = ''

    def handle_text(self, text):
        if self.ignored_parent_count > 0:
            return

        self.current_string += text

    def handle_starttag(self, tag_name):
        # if this tag is the child of an SVE or it is a header element and user would like to ignore headers
        if self.ignored_parent_count > 0:
            if tag_name in SENTENCE_VOID_ELEMENTS or (self.ignore_header_text and tag_name in HEADER_ELEMENTS):
                self.ignored_parent_count += 1
            return

        if tag_name in SENTENCE_VOID_ELEMENTS:
            self.handle_end_of_string()
            self.ignored_parent_count += 1
            return

        if tag_name in BLOCK_LEVEL_ELEMENTS:
            self.handle_end_of_string()
            return

        if tag_name in INLINE_ELEMENTS:
            return

        if self.raise_invalid_tags:
            raise ValueError("Parsing a tag which is not in the accepted element types. It is of type "
                             "{}".format(tag_name))
        else:
            self.ignored_parent_count += 1

    def handle_endtag(self, tag_name):
        if tag_name in SENTENCE_VOID_ELEMENTS or (self.ignore_header_text and tag_name in HEADER_ELEMENTS):
            self.ignored_parent_count -= 1
            self.current_string = ''
            return
                
        # if in an SVE (and this tag is not an SVE).
        if self.ignored_parent_count > 0:
            return

        if tag_name in BLOCK_LEVEL_ELEMENTS:
            self.handle_end_of_string()
            return

        # if tag_name in INLINE_ELEMENTS, nothing is done.

    def handle_empty_tag(self, tag_name):
        if tag_name in EMPTY_ELEMENTS:
            self.handle_end_of_string()
        else:
            raise ValueError(
                "Parsing an empty tag which is not of the accepted element types. It is of type {}".format(tag_name))

    def handle_end_of_string(self):
        self.current_string = self.current_string.strip()

        if len(self.current_string) == 0:
            return

        current_sentences = sent_tokenize(self.current_string)
        for i in current_sentences:
            i = i.strip()
            self.sentences.append(i)

        self.current_string = ''

#Conor O'Sullivan
#26 March 2019
#Functions used in data cleaning and fitting process

#imports
import numpy as np

import json
from IPython.core.display import display, HTML
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import html2text
import ast


#Variables
LIST = ["2","3","5","6","7","8","9","10","11","13","14",
        "18","19","34","35","37","41","46",
        'P1', 'P4', 'P12', 'P7']

class clean:
    #Functions used in cleaning data process

    def getCase(self,ID, path ="/Users/conorosully/Documents/Legal-Case-Prediction/data/preclean/casetext"):
        """
        Returns a case in json format from specified path.
        Required:
        ID: String
        path: Stirng
        """

        path = "{}/{}.json".format(path,ID)
        with open(path) as read_json:
            case = json.load(read_json)
            read_json.close()

        return case

    def renderHTML(self,ID, path ="/Users/conorosully/Documents/Legal-Case-Prediction/data/preclean/casetext"):
        """
        Display case in HTML format
        ID: id of case
        path: path of case
        """

        case = self.getCase(ID)
        case_text = case[ID]

        print("CASE: {}".format(ID))
        print("="*32)
        print()

        return display(HTML(case_text))

    def cleanText(self,text):
        """
        Returns a piece of text after:
        - removed punction
        - made to lower case
        - (stopwords removed when vectorized)
        """
        h = html2text.HTML2Text()
        text_raw = h.handle(text)

        tokens = word_tokenize(text_raw)

        #tokens = [word for word in tokens if word.isalnum()] #remove punctuation
        tokens = [word for word in tokens if word.isalpha()]
        tokens = [w.lower() for w in tokens] #Lower case

        text_clean = " ".join(tokens)

        return text_clean

    #cleans case with a specific form
    def cleanCase(self,case,form):
        """Returns cleaned cases sections"""

        #Procedure
        split_text = case.split(form[0])[1]
        split_text = split_text.split(form[1])
        procedure = self.cleanText(split_text[0])
        split_text = split_text[1]

        #Circumstances
        split_text = split_text.split(form[2])[1]
        split_text = split_text.split(form[3])
        circumstances = self.cleanText(split_text[0])
        split_text = split_text[1]

        #Relevant law
        split_text = split_text.split(form[4])
        relevant = self.cleanText(split_text[0])
        split_text = split_text[1]

        #The facts
        facts = circumstances + relevant

        #The law + other
        split_text = split_text.split(form[5])
        law = self.cleanText(split_text[0])
        other = self.cleanText(split_text[1])

        #full
        full = procedure + circumstances + relevant

        structure = {
        'full':full,
        "procedure":procedure,
        "facts":facts,
        "circumstances":circumstances,
        "relevant":relevant,
        "law":law,
        "other":other}

        return structure

    #Get list of unique articles
    def getUniqueArticles(self,articles):
        """Get list of unique Articles from list of complaints"""

        if type(articles) == float:
            return {}

        articles = ast.literal_eval(articles)
        unique = set() #List of unique articles

        for a in articles:
            sub_articles = a.split("+")
            for s in sub_articles:
                article = s.split("-")[0]
                unique.add(article)

        return(unique)

    # Get Article: 1 if article present, 0 otherwise
    def articleVector(self,articles,violations,nonviolations):
        """Returns vector based on list
        0: nonviolation
        1: violation
        2: other
        -1: no complaint"""

        articles = self.getUniqueArticles(articles)
        violations = self.getUniqueArticles(violations)
        nonviolations = self.getUniqueArticles(nonviolations)

        vector = []
        for l in LIST:
            if l in violations:
                vector.append(1)
            elif l in nonviolations:
                vector.append(0)
            elif l in articles:
                vector.append(2)
            else:
                vector.append(-1)

        return vector



    #check to see if form matches any existing forms
    def getForm(self,case,forms_dict):

        form = ['none', 'none', 'none', 'none', 'none', 'none']
        keys = ['procedure', 'facts', 'circumstances', 'relevant', 'law', 'other']

        #procedure#facts#circumstances#relevant#law#other

        for i,k in enumerate(keys):
            for x in forms_dict[k]:
                #x = " ".join(x.split())
                if x in case:
                    form[i] = x

        return form

    def checkForm(self,form):
        for f in form:
            if f == 'none':
                return False
        return True

    #find the structure of a case
    def printHeadings(self,case,size):


        case_split = case.split("</{}>".format(size))
        for c in case_split:
            print('<{}>'.format(size),end="")
            try:
                heading = c.split("<{}>".format(size))[1]
                print(heading + '</{}>#'.format(size))
            except:
                print('')

    def findHeadings(self,case,size):

        headings = []
        case_split = case.split("</{}>".format(size))
        for c in case_split:
            try:
                s = '<{}>'.format(size) + c.split("<{}>".format(size))[1] + '</{}>'.format(size)
                headings.append(s)
            except:
                x = 1
        return headings




    def __init__(self):
        self.data = []


class classification:

    #Functions used to help classfication model fitting process

    def results(self, y_test, predictions):
        """
        Returns classfification prediction results

        """
        acc = accuracy_score(y_test,predictions)
        cm = confusion_matrix(y_test,predictions)
        cr = classification_report(y_test,predictions)

        print(acc)
        print(cm)
        print(cr)

        return (acc,cm,cr)


    def __init__(self):
        self.data = []

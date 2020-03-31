# Using Machine Learning to Predict Judicial Decisions
A demonstration of the work done for my MSc Computer Science Dissertation. The paper was published in the conference proceedings of the Irish Conference on Artificial Intelligence and Cognitive Science (AICS). 
<br>
<br>
The work looked at predicting the outcome of judicial decisions made by the European Court of Human Rights (ECHR). This was done using Natural Language Processing (NLP) techniques and machine learning. 
<br>
<br>
<b>Publication:</b> <a href="http://aics2019.datascienceinstitute.ie/papers/aics_26.pdf"> here </a>
<br>
<b>Full dissertation:</b>  <a href="https://github.com/conorosully/legal-case-prediction/blob/master/dissertation.pdf"> dissertation.pdf </a>
<br>
<br>
<b>Simplified code demonstration:</b>  <a href="https://github.com/conorosully/legal-case-prediction/blob/master/0%20ECHR%20prediction%20demo.ipynb">0 ECHR prediction demo </a>
<br>
The full project can be found in src folder and the files are described below.
  

<table>
  <tr>
    <th>File</th>
    <th><span style="font-weight:bold">Purpose</span></th>
  </tr>
  <tr>
    <td>functions</td>
    <td>Functions used throughout the project to help with data cleaning and model fitting</td>
  </tr>
  <tr>
    <td>obtain_data</td>
    <td>Obtain raw ECHR data using the API provided by Vizlegal</td>
  </tr>
  <tr>
    <td>preclean_data</td>
    <td>Extract HTML case text and case metadata from raw ECHR data</td>
  </tr>
  <tr>
    <td>clean_dataset</td>
    <td>Clean HTML case text so it is in a format ready to create model features</td>
  </tr>
  <tr>
    <td>clean_attributes</td>
    <td>Clean case metadata so it is in a format ready to create model features</td>
  </tr>
  <tr>
    <td>create_embeddings</td>
    <td>Create word echr2vec embeddings using ECHR documents. This is a novel word embedding created using the word2vec algorithm.</td>
  </tr>
  <tr>
    <td>create_features</td>
    <td>Create N-gram, average word embeddings and pharagraph embeddings feature matrices</td>
  </tr>
    <tr>
    <td>fit_autoML</td>
    <td>Used to train models using the AutoML framework. These are the models presented in the final framework.</td>
  </tr>
  <tr>
    <td>fit_SVM</td>
    <td>Train SVM (initial model prototype)</td>
  </tr>
  <tr>
    <td>fit_CNN</td>
    <td>Train CNN (not in final paper)</td>
  </tr>
  <tr>
    <td>data_visualisations</td>
    <td>Create various visualisations of the dataset</td>
  </tr>
  <tr>
    <td>results_visualisations</td>
    <td>Visualise the model results</td>
  </tr>
  <tr>
    <td>archive (folder)</td>
    <td>Contains all old/ test code</td>
  </tr>
</table>

<br>
Dataset was accessed through an API provided by <a href="https://www.vizlegal.com/#features"> vizlegal </a>. If you are interested in using the ECHR docset for academic reaons feel free to contact them. 



# Using Machine Learning to Predict Judicial Decisions
A demonstration of the work done for my MSc Computer Science dissertation. The paper was published in the conference proceedings of the Irish Conference on Artificial Intelligence and Cognitive Science (AICS). 
<br>
<br>
The work looked at predicting the outcome of judicial decisions made by the European Court of Human Rights (ECHR). This was done using Natural Langugae Processing (NLP) techniques and machine learning. 
<br>
<br>
<b>Publication:</b> <a href="http://aics2019.datascienceinstitute.ie/papers/aics_26.pdf"> here </a>
<br>
<b>Conference proceedings:</b>   <a href="http://aics2019.datascienceinstitute.ie/papers.html"> here </a>
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
    <td>Create word echr2vec embeddings using ECHR documents</td>
  </tr>
  <tr>
    <td>create_features</td>
    <td>Create N-gram, average word embeddings and pharagraph embeddings feature matrices</td>
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
    <td>fit_autoML</td>
    <td>Code used to train models using AutoML framework</td>
  </tr>
  <tr>
    <td>data_visualisations</td>
    <td>Visualise dataset</td>
  </tr>
  <tr>
    <td>results_visualisations</td>
    <td>Visualise model results</td>
  </tr>
  <tr>
    <td>archive (folder)</td>
    <td>Contains all old/ test code</td>
  </tr>
</table>

<br>
Data is not available due to a NDA.

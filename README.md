# Using Machine Learning to Predict Judicial Decisions
A demonstration of the work done for my dissertation for partial completion of a MSc Computer Science. The paper was published in the conference proceedings of the Irish Conference on Artificial Intelligence and Cognitive Science (AICS). 
<br>
<br>
<b>Publication:</b> <a href="http://aics2019.datascienceinstitute.ie/papers/aics_26.pdf"> here </a>
<br>
<b>Conference proceedings:</b>   <a href="http://aics2019.datascienceinstitute.ie/papers.html"> here </a>
<br>
<b>Full dissertation:</b>  <a href="https://github.com/conorosully/legal-case-prediction/blob/master/dissertation.pdf"> dissertation.pdf </a>
<br>
<br>
<a href="https://github.com/conorosully/legal-case-prediction/blob/master/0%20ECHR%20prediction%20demo.ipynb">0 ECHR prediction demo </a>gives a simplied demonstration of the code. The full project can be found in src folder
  

  
 A simplified demonstration of the code can be found 

Code in src folder can be viewed using Jupiter notebooks. Model features and embeddings can be found in the data folder.

The following python notebooks are available in the src folder:

----------------------------

- obtain_data
Used to obtain ECtHR documents using the API provided by Vizlegal

----------------------------

- preclean_data
- clean_dataset
- clean_attributes
Used to clean documents and associated attributes so they are in a suitable form for Feature Engineering 

----------------------------

- create_embeddings
Used to created echr2vec embeddings and doc2vec to models

----------------------------

- create_features
Used to create feature matrices to train models

----------------------------

- fit_SVM
- fit_CNN
- fit_autoML
Used to train models. Only fit_autoML models were considered in the final dissertation

----------------------------

- data_visualisations
- results_visualisations
Used to create visualisations for dissertation

----------------------------

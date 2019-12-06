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
  

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-yla0{font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-yla0">File</th>
    <th class="tg-0lax"><span style="font-weight:bold">Purpose</span></th>
  </tr>
  <tr>
    <td class="tg-0lax">functions</td>
    <td class="tg-0lax">Functions used throughout the project to help with data cleaning and model fitting</td>
  </tr>
  <tr>
    <td class="tg-0lax">obtain_data</td>
    <td class="tg-0lax">Obtain raw ECHR data using the API provided by Vizlegal</td>
  </tr>
  <tr>
    <td class="tg-0lax">preclean_data</td>
    <td class="tg-0lax">Extract HTML case text and case metadata from raw ECHR data</td>
  </tr>
  <tr>
    <td class="tg-0lax">clean_dataset</td>
    <td class="tg-0lax">Clean HTML case text so it is in a format ready to create model features</td>
  </tr>
  <tr>
    <td class="tg-0lax">clean_attributes</td>
    <td class="tg-0lax">Clean case metadata so it is in a format ready to create model features</td>
  </tr>
  <tr>
    <td class="tg-0lax">create_embeddings</td>
    <td class="tg-0lax">Create word echr2vec embeddings using ECHR documents</td>
  </tr>
  <tr>
    <td class="tg-0lax">create_features</td>
    <td class="tg-0lax">Create N-gram, average word embeddings and pharagraph embeddings feature matrices</td>
  </tr>
  <tr>
    <td class="tg-0lax">fit_SVM</td>
    <td class="tg-0lax">Train SVM (initial model prototype)</td>
  </tr>
  <tr>
    <td class="tg-0lax">fit_CNN</td>
    <td class="tg-0lax">Train CNN (not in final paper as I ran out of time)</td>
  </tr>
  <tr>
    <td class="tg-0lax">fit_autoML</td>
    <td class="tg-0lax">Code used to train models using AutoML framework</td>
  </tr>
  <tr>
    <td class="tg-0lax">data_visualisations</td>
    <td class="tg-0lax">Visualise dataset</td>
  </tr>
  <tr>
    <td class="tg-0lax">results_visualisations</td>
    <td class="tg-0lax">Visualise model results</td>
  </tr>
</table>

<br>
Data is not available due to a NDA.

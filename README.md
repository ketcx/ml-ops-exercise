<h1 align='center'>Operationalizing Machine Learning</h1>
<p align="center">Armando Medina</p>
<p align="center">(December, 2020)</p>

<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/diagram.png" width=600>
</p>

## Project Overview

<p>In this project, we are going to continue working with the banking marketing dataset. We are going to use Azure to set up a cloud-based machine learning production model, deploy it, and consume it. You'll also create, publish, and consume a pipeline.</p>

<p>Main steps of the project:

1. Authentication
2. Automated ML Experiment
3. Deploy the best model
4. Enable logging
5. Swagger Documentation
6. Consume model endpoints
7. Create and publish a pipeline
8. Documentation

</p>

## 1. Authentication

<p>In this step, I install Azure Machine Learning Extension which allows you to interact with Azure Machine Learning Studio, which is part of the az command.

After you have the Azure Machine Learning Extension, create a service principal account and then associate it with the specific workspace.</p>

<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img001.png" width=600>
</p>

## 2. Automated ML Experiment

<p>In this step, I will create an experiment using automated machine learning and then configure a compute cluster and use that cluster to run the experiment.</p>
<br />
<p align="center">Data set registered in Azure ML from a url.</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img002.png" width=600>
  
</p>
<br />
<p align="center">We apply AutoML to our dataset. Here is the completed experiment.</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img003.png" width=600>  
</p>
<br />
<p align="center">Here we see the best model of our experiment: MaxAbSacler, XGBoostClasssifier.</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img004.png" width=600>  
</p>

## 3. Deploy the best model

<p>In this step, implement the best model to be able to interact with the HTTP API service and interact with the model by sending data through POST requests.</p>

## 4. Enable logging

<p>Now that the best model has been implemented, enable Application Insights and retrieve the logs through a script.</p>

<p align="center">Here we see "Application Insights" enable inthe deatials tab of the endpoint.</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img005.png" width=600>  
</p>

<p align="center">Here we see the output when you run logs.py.</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img006.png" width=600>  
</p>

## 5. Swagger Documentation

<p>In this step, you will consume the deployed model using Swagger.</p>

<p align="center">Here we see swagger run on localhost showing the HTTP API methods and reponse for the model.</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img007.png" width=600>  
</p>

## 6. Consume model endpoints

<p>In this step I used the provided endpoint.py script to interact with the trained model.</p>

<p align="center">Here we see the output of endpoint.py.</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img008.png" width=600>  
</p>

<p align="center">Here we see the output of Apache Benchmark run against the HTTP API.</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img009.png" width=600>  
</p>

<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img010.png" width=600>  
</p>

## 7. Create and publish a pipeline

<p align="center">This step shows our work with:

- The pipeline section of Azure ML studio, showing that the pipeline has been created.
- The pipelines section in Azure ML Studio, showing the Pipeline Endpoint.
- The Bankmarketing dataset with the AutoML module
- The “Published Pipeline overview”, showing a REST endpoint and a status of ACTIVE.
- In Jupyter Notebook, showing that the “Use RunDetails Widget” shows the step runs.
- In ML studio showing the scheduled run.

</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img011.png" width=600>  
</p>s
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img012.png" width=600>  
</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img013.png" width=600>  
</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img014.png" width=600>  
</p>

<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img015.png" width=600>  
</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img016.png" width=600>  
</p>
<p align="center">
  <img src="https://github.com/ketcx/ml-ops-exercise/blob/master/data/img017.png" width=600>  
</p>

## 8. Screencast

## 9. Future Works

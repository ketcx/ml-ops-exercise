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

## 4. Enable logging

## 5. Swagger Documentation

## 6. Consume model endpoints

## 7. Create and publish a pipeline

## 8. Documentation

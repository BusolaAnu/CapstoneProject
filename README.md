*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Your Project Title Here
Capstone Project for Nanodegree program on Udacity. In this project, two models was created one using Automated ML and the other a customized model whose hyperparameters are tuned using HyperDrive on an external dataset.

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.
To set up this project,
1. Create a compute instance in AzureML studio
2. Provide a link to your dataset or resgister your dataset on AzureML
3. Model Building:
  AutoML
    1. Set up AutoML configuration
    2. Run the AutoML configuration and get your best model and best run
  Hyperdrive 
    1. Set up Hyperdrive configuration
    2. Run the Hyperdrive configuration and save your best model and best run
4. Model Deployment: Deploy your best model as a webservice
5. Consume the endpoint using the rest uri and primary key.
 
## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.
The data used in this project is the Heart falure dataset available on kaggle. The dataset contains 12 features that can be used to predict mortality by heart failure.
These features includes behavioural lifestyles that could increase the risk of heart failure such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol. 

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.
The heart failure dataset will be used to build a classification model to predict either an occurence of death(1) or not(0) based on the following features: 
age, anaemia, creatinine_phosphokinase, diabetes,	ejection_fraction,	high_blood_pressure,	platelets	serum_creatinine,	serum_sodium,	sex,	smoking and time


### Access
*TODO*: Explain how you are accessing the data in your workspace.
A link to the dataset is provided in the notebook and it was accessed using the tabular datafactory function

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

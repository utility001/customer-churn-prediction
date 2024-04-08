# Customer Churn Prediction Model

## Overview
This project aims to develop a machine learning model to predict customer churn for a telecommunication company.  
Customer churn (aka customer attrition) refers to the phenomenon of customers ceasing to do use that telecom provider anymore.
Predicting customer churn is a crucial task that enables businesses to identify at-risk customers and take proactive measures to retain them.

## Features
- The model uses a variety of customer-related features, such as:
  - Number of months the customer has been with the current telco provider
  - Total minutes of day calls.
  - Number of voicemail messages
  - Number of customer service calls etc as described in data_description.md file

## Data
- The dataset used for training the model was gotten from [kaggle](https://www.kaggle.com/competitions/customer-churn-prediction-2020/data)
- The features are preprocessed and cleaned to ensure data quality and consistency.
- Exploratory data analysis (EDA) is performed to gain insights into the dataset and identify patterns.

## Model Building
- The model is built using a decision tree to foster explainability.
- Hyperparameter tuning was also performed to optimize model performance and generalization.
- Evaluation metrics, such as precision, recall, and F1-score, were used to assess model performance.

## Future Improvements
- Deployment to a live environment to enable interaction.
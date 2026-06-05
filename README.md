Customer Purchase Prediction Using Decision Tree and Random Forest
Project Overview

This project focuses on predicting whether a customer is likely to make a purchase based on demographic and behavioral data. Machine Learning classification algorithms, namely Decision Tree and Random Forest, are used to analyze customer attributes and predict purchase decisions.

The system helps businesses understand customer behavior and identify potential buyers, enabling more effective marketing strategies and improved customer engagement.

Features
Customer purchase prediction using Machine Learning
Data preprocessing and feature encoding
Implementation of Decision Tree Classifier
Implementation of Random Forest Classifier
Model performance evaluation using Accuracy Score and Classification Report
Prediction for new customer records
Easy-to-understand and beginner-friendly implementation
Dataset Attributes

The dataset contains the following features:

Attribute	Description
Name	Customer Name
Age	Customer Age
Gender	Male/Female
Income	Annual Income
WebsiteVisit	Number of Website Visits
PreviousPurchase	Number of Previous Purchases
Purchase	Target Variable (Yes/No)
Technologies Used
Python
Pandas
Scikit-learn
NumPy
Jupyter Notebook / VS Code
Machine Learning Algorithms
Decision Tree

A supervised learning algorithm that creates a tree-like structure to make classification decisions based on feature values.

Random Forest

An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

Project Workflow
Load customer dataset
Clean and preprocess data
Encode categorical variables
Split dataset into training and testing sets
Train Decision Tree model
Train Random Forest model
Evaluate model performance
Predict purchase behavior for new customers
Installation

Clone the repository:

git clone https://github.com/your-username/customer-purchase-prediction.git

Navigate to the project folder:

cd customer-purchase-prediction

Install required dependencies:

pip install pandas scikit-learn numpy
Usage

Run the Decision Tree model:

python decision_tree.py

Run the Random Forest model:

python random_forest.py
Sample Prediction

Input:

Age: 30
Gender: Male
Income: 55000
Website Visits: 12
Previous Purchases: 3

Output:

Customer will Purchase
Results

The project compares the performance of Decision Tree and Random Forest models using:

Accuracy Score
Precision
Recall
F1-Score
Classification Report

Typically, Random Forest provides better accuracy and generalization compared to a single Decision Tree.

Future Enhancements
Larger real-world customer datasets
Hyperparameter tuning
Feature importance visualization
Web application deployment using Flask or Streamlit
Integration with e-commerce platforms
Advanced algorithms such as XGBoost and Gradient Boosting
Learning Outcomes
Understanding supervised machine learning
Working with customer behavioral data
Implementing classification algorithms
Evaluating model performance
Building predictive analytics solutions
License

This project is open-source and available under the MIT License.

# Diabetes Patients Prediction


This project aims to predict whether a patient has diabetes based on certain diagnostic measurements. The dataset used is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. All patients in this dataset are females, at least 21 years old, of Pima Indian heritage.

## Dataset Overview

### Columns:

- **Pregnancies**: Number of pregnancies
- **Glucose**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- **Blood Pressure**: Diastolic blood pressure (mm Hg)
- **Skin Thickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **Diabetes Pedigree Function**: Diabetes pedigree function
- **Age**: Age (years)
- **Outcome**: 1 if the person has diabetes, 0 otherwise

## Data Preprocessing

- Handling missing values.
- Replacing zero values in certain columns with the mean.

## Exploratory Data Analysis

- Calculating and visualizing the correlation matrix.

## Model Training and Evaluation

- Splitting the data into training and testing sets.
- Training Logistic Regression, Decision Tree, Random Forest, and Support Vector Machine (SVM) models.

### Model Accuracy:

- **Logistic Regression**: {accuracy_lr:.2%}
- **Decision Tree**: {accuracy_dt:.2%}
- **Random Forest**: {accuracy_rf:.2%}
- **SVM**: {accuracy_svm:.2%}

## Confusion Matrix Visualization

- Displaying confusion matrices for each model.

## Model Persistence

The trained Logistic Regression model is saved using joblib for future use.

Feel free to explore and contribute to the project!

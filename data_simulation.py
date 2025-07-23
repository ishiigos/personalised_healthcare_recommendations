import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)

# Number of rows
n = 2500

# Helper functions
def diet_type():
    return np.random.choice(['Vegan', 'Vegetarian', 'Keto', 'Standard', 'Mediterranean'], n)

def smoking_status():
    return np.random.choice(['Non-smoker', 'Current smoker', 'Ex-smoker'], n)

def alcohol_level():
    return np.random.choice(['None', 'Low', 'Moderate', 'High', np.nan], n, p=[0.3, 0.3, 0.2, 0.1, 0.1])

def occupation_type():
    return np.random.choice(['Office Worker', 'Manual Laborer', 'Healthcare', 'Educator', 'Unemployed', 'Retired'], n)

def marital_status():
    return np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'], n)

def education_level():
    return np.random.choice(['No Formal Education', 'High School', 'Bachelor', 'Master', 'PhD'], n)

def flu_vaccine_status():
    return np.random.choice([0, 1], n, p=[0.3, 0.7])

# Simulated dataset
df = pd.DataFrame({
    'Patient_ID': np.arange(1, n+1),
    'Age': np.random.randint(18, 90, n),
    'Gender': np.random.choice(['Male', 'Female'], n),
    'BMI': np.round(np.random.normal(25, 5, n), 1),
    'Smoking_Status': smoking_status(),
    'Alcohol_Consumption': alcohol_level(),
    'Physical_Activity_Level': np.random.choice(['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active'], n),
    'Diet_Type': diet_type(),
    'Cholesterol': np.round(np.random.normal(200, 25, n), 1),
    'Glucose_Level': np.round(np.random.normal(100, 15, n), 1),
    'HbA1c': np.round(np.random.normal(5.5, 1, n), 2),
    'Heart_Disease_Risk': np.round(np.random.uniform(0, 1, n), 2),
    'Diabetes_Risk': np.round(np.random.uniform(0, 1, n), 2),
    'Health_Risk': np.round(np.random.uniform(0, 1, n), 2),
    'Predicted_Insurance_Cost': np.round(np.random.normal(12000, 2500, n), 2),
    'Diet_Recommendation': np.random.choice(['Low Carb', 'High Protein', 'Balanced', 'Plant-Based'], n),
    'Exercise_Recommendation': np.random.choice(['Cardio', 'Strength Training', 'Yoga', 'Walking'], n),
    'PRS_Cardiometabolic': np.round(np.random.normal(0.5, 0.1, n), 3),
    'PRS_Type2Diabetes': np.round(np.random.normal(0.4, 0.1, n), 3),
    'APOE_e4_Carrier': np.random.choice([0, 1], n, p=[0.8, 0.2]),
    'BRCA_Pathogenic_Variant': np.random.choice([0, 1], n, p=[0.9, 0.1]),
    'Family_History_CVD': np.random.choice([0, 1], n),
    'Family_History_T2D': np.random.choice([0, 1], n),
    'Stress_Level': np.round(np.random.uniform(1, 10, n), 1),
    'Depression_Score': np.round(np.random.normal(5, 2, n), 1),
    'Anxiety_Score': np.round(np.random.normal(5, 2, n), 1),
    'Sleep_Hours': np.round(np.random.normal(7, 1.5, n), 1),
    'Sleep_Quality': np.round(np.random.uniform(1, 10, n), 1),
    'Resting_Heart_Rate': np.random.randint(55, 90, n),
    'HRV': np.random.randint(20, 80, n),
    'Systolic_BP': np.random.randint(100, 160, n),
    'Diastolic_BP': np.random.randint(60, 100, n),
    'LDL': np.round(np.random.normal(120, 20, n), 1),
    'HDL': np.round(np.random.normal(50, 10, n), 1),
    'Triglycerides': np.round(np.random.normal(150, 50, n), 1),
    'CRP': np.round(np.random.normal(1.0, 0.5, n), 2),
    'eGFR': np.round(np.random.normal(100, 15, n), 1),
    'Occupation': occupation_type(),
    'Marital_Status': marital_status(),
    'Education_Level': education_level(),
    'Annual_Income': np.round(np.random.normal(50000, 15000, n), 2),
    'On_Statins': np.random.choice([0, 1], n, p=[0.85, 0.15]),
    'On_Antihypertensives': np.random.choice([0, 1], n, p=[0.8, 0.2]),
    'Flu_Vaccine_Last_Year': flu_vaccine_status(),
    'PRS_Alzheimers': np.round(np.random.normal(0.3, 0.1, n), 3),
    'Waist_Hip_Ratio': np.round(np.random.normal(90, 10, n) / np.random.normal(100, 10, n), 2)
})

# Previewoc
print(df.head())

# Save to CSV
df.to_csv('health_data.csv', index=False)
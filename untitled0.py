# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:36:53 2023

@author: ikbel
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm

# Load Data
# Data used is the Home Equity Loans (HMEQ)
dat = pd.read_csv("hmeq.csv")

# Print column names to verify if they match the names used in the loan_recommendation function
#print(dat.columns)

# Function to determine loan recommendation based on risk levels
def loan_recommendation(row):
    if row['DELINQ'] == 0 and row['DEBTINC'] < 30 and row['CLNO'] >= 5:
        return 'APPROVED'
    elif row['DELINQ'] <= 2 and row['DEBTINC'] < 40 and row['CLNO'] >= 3:
        return 'CONDITIONAL APPROVED'
    else:
        return 'REJECT'

# Apply the function to create a new column 'LoanRecommendation'
dat['LoanRecommendation'] = dat.apply(loan_recommendation, axis=1)

# Print or inspect the DataFrame with the new 'LoanRecommendation' column
print(dat.head())

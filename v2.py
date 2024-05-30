import pandas as pd

# Load Data
# Assuming "hmeq.csv" is in the same directory as your script or notebook
dat = pd.read_csv("hmeq.csv")

# Function to determine loan recommendation based on risk levels
def loan_recommendation(row):
    # Adjust column names and criteria based on your dataset
    if row['DELINQ'] == 0 and row['DEBTINC'] < 30 and row['CLNO'] >= 5:
        return 'LOW RISK - APPROVED'
    elif row['DELINQ'] <= 2 and row['DEBTINC'] < 40 and row['CLNO'] >= 3:
        return 'MEDIUM RISK - CONDITIONAL APPROVED'
    else:
        return 'HIGH RISK - REJECT'

# Apply the function to create a new column 'LoanRecommendation'
dat['LoanRecommendation'] = dat.apply(loan_recommendation, axis=1)

# Print or inspect the DataFrame with the new 'LoanRecommendation' column
print(dat.head())

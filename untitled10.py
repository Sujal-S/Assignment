# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = 'assignment.csv'
df = pd.read_csv(file_path) 

df['Time'] = pd.to_datetime(df['Time'], format='%m/%d/%Y %I:%M %p')
df['Time Out'] = pd.to_datetime(df['Time Out'], format='%m/%d/%Y %I:%M %p')

# Group data by employee name
grouped = df.groupby('Employee Name')

# Iterate over each employee's group
for name, group in grouped:
    # Calculate the difference in days between consecutive entries
    consecutive_days = group['Time'].diff().dt.days.fillna(0)
    # Check if there are 7 consecutive days
    if (consecutive_days >= 7).any():
        print(f"{name} has worked for 7 consecutive days.")

grouped = df.groupby('Employee Name')

# Iterate over each employee's group
for name, group in grouped:
    # Calculate the time difference between consecutive shifts
    time_between_shifts = (group['Time'] - group['Time Out'].shift()).dt.total_seconds() / 3600
    # Check if there are shifts with less than 10 hours but greater than 1 hour between them
    if ((time_between_shifts > 1) & (time_between_shifts < 10)).any():
        print(f"{name} has less than 10 hours between shifts but greater than 1 hour.")

df['Shift Duration'] = (df['Time Out'] - df['Time']).dt.total_seconds() / 3600

# Filter employees who have worked for more than 14 hours in a single shift
filtered_df = df[df['Shift Duration'] > 14]

# Print the names of employees who meet the criteria
for index, row in filtered_df.iterrows():
    print(f"{row['Employee Name']} has worked for more than 14 hours in a single shift.")
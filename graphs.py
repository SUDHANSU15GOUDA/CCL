import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from preprocessing import dataframe

# print(dataframe)


#1
def workclass(df):
    work = df['workclass'].value_counts().head()
    
    df = round((df['workclass'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Workclass', 'workclass': 'percent'})
    return df

#2  
def education(df):
    edu = df['education'].value_counts().head(3)
    
    df = round((df['education'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Education', 'education': 'Percent'})
    return df

#3  
def marital_status(df):
    status = df['marital_status'].value_counts()
    
    df = round((df['marital_status'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Marital Status', 'marital_status': 'Percent'})
    return df

# print(marital_status(dataframe))

#4
def gender(df):
    g = df['sex'].value_counts()
    
    df = round((df['sex'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Gender', 'sex': 'Percent'})
    return df
#5
def income(df):
    inc = df['salary'].value_counts()
    
    df = round((df['salary'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Salary', 'salary': 'Percent'})
    return df







def work_graph(df):
    return df['workclass'].value_counts()

def education_graph(df):
    return df['education'].value_counts()

def marital_status_graph(df):
    return df['marital_status'].value_counts()

def gender_graph(df):
    return df['sex'].value_counts()

def salary_graph(df):
    return df['salary'].value_counts()





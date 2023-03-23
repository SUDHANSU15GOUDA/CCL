import pandas as pd
import numpy as np

dataframe = pd.read_csv('adult.csv')
print(dataframe)

def column_edit_education(studied):
    
    if (studied==' 11th') | (studied==' 9th') | (studied==' 7th-8th') | (studied==' 5th-6th') | (studied==' 10th') | (studied==' 1st-4th') | (studied==' Preschool') | (studied==' 12th'):
        return 'Lower'
    else:
        return studied
    
dataframe['education']=dataframe['education'].apply(column_edit_education)

def column_edit_marital_status(status):
    if (status==' Never-married') | (status==' Divorced') | (status==' Separated') | (status==' Widowed') :
        return 'not-married'
    else:
        return 'married'
    
dataframe['marital-status']=dataframe['marital-status'].apply(column_edit_marital_status)

def column_edit_hrs_per_week(hrs):
    if (0 < hrs < 10):
      return '<10'
    elif (10 <= hrs <= 20):
      return 'between 10,20'
    elif (21 <= hrs <= 30):
      return 'between 21,30'
    elif (31 <= hrs <= 40):
      return 'between 31,40'
    elif (41 <= hrs <= 50):
      return 'between 41,50'
    elif (51 <= hrs <= 60):
      return 'between 51,60'
    elif (61 <= hrs <= 70):
      return 'between 61,70'
    elif (71 <= hrs <= 80):
      return 'between 71,80'
    elif (81 <= hrs <= 90):
      return 'between 81,90'
    elif (91 <= hrs <= 100):
      return 'between 91,100'
    else:
      return '>100'
  
dataframe['hours-per-week'] = dataframe['hours-per-week'].apply(column_edit_hrs_per_week)

def column_edit_salary(inc):
    if inc ==  ' <=50K':
        return 'Income less than 50K'
    else:
        return 'Income More then 50K'
    
dataframe['salary'] = dataframe['salary'].apply(column_edit_salary)

dataframe['hours-per-week'].unique()

dataframe[dataframe == ' ?'] = np.nan

dataframe.dropna(inplace = True)

dataframe.rename(columns = {'hours-per-week':'hours_per_week'}, inplace = True)
dataframe.rename(columns = {'marital-status':'marital_status'}, inplace = True)

print(dataframe)
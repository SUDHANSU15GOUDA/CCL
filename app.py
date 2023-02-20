
import streamlit as st 
import pickle
import pandas as pd

m = pickle.load(open('random_f.pkl','rb'))

workclass = [' State-gov', ' Self-emp-not-inc', 
             ' Private', ' Federal-gov',
             ' Local-gov', ' Self-emp-inc', ' Without-pay']

education = [' Bachelors', ' HS-grad', 'Lower', 
             ' Masters', ' Some-college',
             ' Assoc-acdm', ' Doctorate', 
             ' Assoc-voc', ' Prof-school']

marital_status = ['not-married', 'married']

occupation = [' Adm-clerical', ' Exec-managerial',
              ' Handlers-cleaners',' Prof-specialty',
              ' Other-service', ' Sales', ' Transport-moving',
              ' Farming-fishing', ' Machine-op-inspct', 
              ' Tech-support',' Craft-repair', ' Protective-serv',
              ' Armed-Forces',' Priv-house-serv']

sex = [' Male', ' Female']

hours_per_week = ['between 31,40', 'between 10,20', 'between 41,50',
                  'between 71,80','between 21,30', 'between 51,60',
                  'between 61,70', '<10','between 91,100', 'between 81,90']





random_f = pickle.load(open('random_f.pkl','rb'))



st.title("Income Prediction Classifier")




col1, col2 = st.columns(2)

with col1:
    select_workclass = st.selectbox('Select Workclass',sorted(workclass))
    
with col2:
    select_education = st.selectbox('Select Education',sorted(education))
    
    
    
    
select_occupation = st.selectbox('Select Occupation',sorted(occupation))
    
    
    
    
col5, col6 = st.columns(2)
    
with col5:
    select_sex = st.selectbox('Select Sex',sorted(sex))
    
with col6:
    select_hours_per_week = st.selectbox('Select Hours Per Week',sorted(hours_per_week))
    

col7, col8 = st.columns(2)

with col7:
    select_age = st.number_input('Enter Age')
    
with col8:
    select_marital_status = st.selectbox('Select Marital Status',sorted(marital_status))
    
    
    
    
    
if st.button('Predict'):
    input_df = pd.DataFrame({'age':[select_age],'workclass':[select_workclass],'education':[select_education],
                             'marital_status':[select_marital_status],'occupation':[select_occupation],
                             'sex':[select_sex],'hours_per_week':[select_hours_per_week]})

    #st.table(input_df)
    result = random_f.predict(input_df)
    result_percentage = random_f.predict_proba(input_df)
    
    st.title('Predicted Outcome...')
    st.header(result[0])
    
    
    
    
    st.title("To be more precise....") 
    
    f = result_percentage[0][0]
    s = result_percentage[0][1]
    
    st.header("Chances of Income more than 50K : "+str(round(f*100,2))+"%")
    st.header("Chances of Income less than 50K : "+str(round(s*100,2))+"%")
    
       
    


  

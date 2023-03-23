import numpy as np
import streamlit as st 
from streamlit_option_menu import option_menu
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from preprocessing import dataframe
import graphs



with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Predection Page", "Dataset", "Models & Accuracy"]
    )


if selected == 'Predection Page':




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
        
        if result[0] == 'Income less than 50K':
            st.info('Income less than ₹50,000')
        else:
            st.info('Income more than ₹50,000')
        
        
        
        st.title("To be more precise....") 
        
        f = result_percentage[0][0]
        s = result_percentage[0][1]
        
        st.success("Chances of Income more than 50K : "+str(round(f*100,2))+"%")
        st.error("Chances of Income less than 50K : "+str(round(s*100,2))+"%")
        
        
        # Visuals of Dataset

        d = dataframe
        
        
        
        
        col31, col32 = st.columns(2)
        
        with col31:
            workclass_output = graphs.workclass(d)
            
        
            st.title("Workclass")
            st.dataframe(workclass_output)
        
        with col32:
            work_graph = graphs.work_graph(d)
            st.title("Bar Chart")
            fig, ax = plt.subplots()
            ax.barh(work_graph.index,work_graph.values)
            plt.legend()
            st.pyplot(fig)
            
        
        
        
        
        
        col41, col42 = st.columns(2)
        
        with col41:
            education_output = graphs.education(d)
            
        
            st.title("Education")
            st.dataframe(education_output)
            
        with col42:
            education_graph = graphs.education_graph(d)
            st.title("Bar Chart")
            fig, ax = plt.subplots()
            ax.barh(education_graph.index,education_graph.values)
            plt.legend()
            st.pyplot(fig)
            
            
            
            
        
        col51, col52 = st.columns(2)
        
        with col51:
            marital_status_output = graphs.marital_status(d)
        
            st.title("Marital Status")
            st.dataframe(marital_status_output)
            
        with col52:
            marital_status_graph = graphs.marital_status_graph(d)
            st.title("Pie Chart")
            fig, ax = plt.subplots()
            ax.pie(marital_status_graph.values, shadow = True, explode = [0.1,0.1], colors = ['r','g'], autopct='%1.1f%%')
            st.pyplot(fig)
            
            
            
            
            
        
        
        
        col61, col62 = st.columns(2)
        
        with col61:
            income_output = graphs.income(d)
        
            st.title("Income")
            st.dataframe(income_output)
            
        with col62:
            salary_graph = graphs.salary_graph(d)
            st.title("Pie Chart")
            fig, ax = plt.subplots()
            ax.pie(salary_graph.values, shadow = True, explode = [0,0.2], colors = ['c','blue'], autopct='%1.1f%%')
            st.pyplot(fig)
            
            
            
        
        
        col71, col72 = st.columns(2)
        
        with col71:
            
            gender_output = graphs.gender(d)
        
            st.title("Gender")
            st.dataframe(gender_output)
            
        with col72:
            gender_graph = graphs.gender_graph(d)
            st.title("Pie Chart")
            fig, ax = plt.subplots()
            ax.pie(gender_graph.values, shadow = True, explode = [0.2,0], colors = ['#4CAF50','#100CAF50'], autopct='%1.1f%%')
            st.pyplot(fig)
            
            
            





if selected == 'Dataset':
    
    data = pd.read_csv('adult.csv')
    show = data.head()
    show2 = data.tail()
    show3 = data.columns
    show4 = data.describe().T
    
    
    
    st.title('First 5 Values of the Dataset...')
    
    st.table(show)
    
    
    
    st.title('Last 5 Values of the Dataset...')
    
    st.table(show2)
    
    
    
    
       
    st.title('Columns of the Dataset...')
    
    st.table(show3)
        
        
           
    st.title('Description of the Dataset...')
    
    st.table(show4)
 
 
 
 
 
 
 
if selected == 'Models & Accuracy':
    
    st.title('Logistic Regression')
    
    st.info('Gives us 78.21%, accuracy')
    
    
    
    st.title('KNeighborsClassifier')
    
    st.info('Gives us 79.91%, accuracy')
    
    
    
    st.title('Naive Bayes')
    
    st.info('Gives us 76.41%, accuracy')
    
    
    
    st.title('Decision Tree Classifier')
    
    st.info('Gives us 77.19%, accuracy')
    
    
    
    st.title('Random Forest Classifier')
    
    st.info('Gives us 81.68%, accuracy')
    
    
    
    
    
    
    
    
    
    
    
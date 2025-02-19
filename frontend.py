import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models



heart_attack_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart Attack Prediction System',

                           [
                            'Heart Disease Prediction'
                            ],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)




# Heart Disease Prediction Page
if selected == 'Heart Attack  Prediction':

    # page title
    st.title('Heart Attack Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        BMI = st.text_input('BMI')

    with col3:
        HighRiskLastYear = st.text_input('High Risk Last Year')

    with col1:
        HadStroke = st.text_input('Had Stroke')

    with col2:
        HadDepressiveDisorder = st.text_input('Had Depressive Disorder')

    with col3:
        SmokeStatus = st.text_input('Smoke Status')

    
    

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


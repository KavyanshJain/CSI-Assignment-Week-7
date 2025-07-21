import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('model/best_model.pkl')

# Define the input fields
st.title('Adult Census Income Prediction')

age = st.number_input('Age', min_value=0, max_value=100, value=30)
workclass = st.selectbox('Workclass', ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'])
education_num = st.number_input('Education-num', min_value=1, max_value=16, value=10)
marital_status = st.selectbox('Marital-status', ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'])
occupation = st.selectbox('Occupation', ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'])
relationship = st.selectbox('Relationship', ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
sex = st.selectbox('Sex', ['Male', 'Female'])
capital_gain = st.number_input('Capital-gain', min_value=0, value=0)
capital_loss = st.number_input('Capital-loss', min_value=0, value=0)
hours_per_week = st.number_input('Hours-per-week', min_value=0, max_value=100, value=40)

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'Age': [age],
    'Workclass': [workclass],
    'EducationNum': [education_num],  # Corrected
    'Marital Status': [marital_status],
    'Occupation': [occupation],
    'Relationship': [relationship],
    'Gender': [sex],  # Corrected
    'Capital Gain': [capital_gain],
    'capital loss': [capital_loss],
    'Hours per Week': [hours_per_week]
})

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.success("Income <= 50K")
    else:
        st.success("Income > 50K 🎉")

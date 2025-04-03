import streamlit as st
import  joblib
import pandas as pd
import numpy as np



# Load the model from the file
model = joblib.load('yield_model')
preprocessor = joblib.load('preprocessor')

data = pd.read_csv('yield_data.csv')

# load the area
area = data['Area'].unique()

# load the items
items = data['Item'].unique()

# load year
year = data['Year'].unique()

st.title('🌾 Crop Yield Production Analysis')


with st.form(key='crop'):
    year = st.selectbox('Year', year)
    average_rain_fall = st.number_input('Average Rainfall/per(mm)')
    pesticides_tonnes = st.number_input('Pesticides Tonnes')
    avg_temp = st.number_input('Average Temperature')
    Area = st.selectbox('Select Area', area)
    Item = st.selectbox('Item', items)
 


    # Submit button for the form
    submit_button = st.form_submit_button(label="Predict Yield",use_container_width=True,)

if submit_button:
    # Validation logic
    if (year == 0 and average_rain_fall == 0.0 and avg_temp == 0.0 and not Area and not Item):
        st.error("Please fill in all fields with valid inputs before submitting!",icon="🚨")
    else:
        # Prepare the features
        features = np.array([year, average_rain_fall, pesticides_tonnes, avg_temp,Area,Item]).reshape(1, -1)
        data_transformed = preprocessor.transform(features)

        # Predict the yield
        result = model.predict(data_transformed)[0]
        st.success(f'Predicted Yield: {result:,.0f} tonnes')
        st.balloons()
import pandas as pd
import streamlit as st
import joblib


model = joblib.load("xgb_model_jb")  

st.title("🏠 House Price Prediction")
st.write("Enter the details below to predict the house price.")


inputs = [
    'OverallQual','GrLivArea','FullBath', 'YearBuilt','GarageYrBlt','CentralAir'
]

input_data = {}

for feature in inputs:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox(
            feature, options=['yes', 'no'], index=0
        )
    else:
        input_data[feature] = st.number_input(
            feature,
            value=0.0,
            step=1.0 if feature in ['OverallQual', 'FullBath','CentralAir'] else 0.1
        )

# Predict button
if st.button("Predict Price"):
    
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == "yes" else 0
    
    input_df = pd.DataFrame([input_data], columns=inputs)

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted House Price: ${prediction:,.2f}")






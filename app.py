import streamlit as st
import requests

# Streamlit UI
st.title("Car Price Predictor")

# Input form for user
year = st.slider("Year", 2000, 2023, 2020)
present_price = st.number_input("Present Price", min_value=0.0, value=5.0)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=50000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.number_input("Owner", min_value=0, value=0)

# Predict button
if st.button("Predict"):
    # Prepare data for API request
    input_data = {
        "Year": year,
        "Present_Price": present_price,
        "Kms_Driven": kms_driven,
        "Fuel_Type": fuel_type,
        "Seller_Type": seller_type,
        "Transmission": transmission,
        "Owner": owner,
    }

    # Make API request
    response = requests.post("http://localhost:8000/predict", json=input_data)

    # Display prediction
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Price: {result['predicted_price']}")
    else:
        st.error("Error making prediction. Please try again.")

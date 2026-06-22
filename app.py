import streamlit as st
from crop_model import predict_crop


# Page settings
st.set_page_config(
    page_title="AI Smart Agriculture Assistant",
    page_icon="🌱"
)


# Title
st.title("🌱 AI Smart Agriculture Assistant")

st.write(
"""
An AI-powered system that recommends suitable crops
based on soil nutrients and environmental conditions.
"""
)


st.divider()


st.header("🌾 Enter Farm Details")


# Inputs

nitrogen = st.number_input(
    "Nitrogen (N)",
    min_value=0
)

phosphorus = st.number_input(
    "Phosphorus (P)",
    min_value=0
)

potassium = st.number_input(
    "Potassium (K)",
    min_value=0
)

temperature = st.number_input(
    "Temperature (°C)"
)

humidity = st.number_input(
    "Humidity (%)"
)

ph = st.number_input(
    "Soil pH"
)

rainfall = st.number_input(
    "Rainfall (mm)"
)


st.divider()


if st.button("🔍 Predict Best Crop"):

    result = predict_crop(
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    )


    st.success(
        f"🌱 Recommended Crop: {result.upper()}"
    )


    st.info(
        """
        Farming Tips:
        
        ✅ Maintain proper irrigation  
        ✅ Monitor soil nutrients regularly  
        ✅ Use sustainable farming methods
        """
    )
import streamlit as st
from app.config import api_key
from google.generativeai import GenerativeModel

st.title("Tweet Generator - V 🐦")
st.subheader("🚀 Generate tweets on any topic")

# User input fields
topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

# st.write(f"Debug API Key: {api_key}")

# Initialize Gemini model
gemini_model = GenerativeModel("gemini-2.0-flash")  # Use the latest model

if st.button("Generate"):
    prompt = f"Generate {number} of tweets about {topic} without hash tags."
    
    try:
        response = gemini_model.generate_content(prompt)  # Correct way to invoke Gemini API
        
        # Extract text from response
        if hasattr(response, 'text'):
            st.write(response.text)
        else:
            st.write(response)  # Fallback if response is a simple string
    
    except Exception as e:
        st.error(f"Error: {e}")

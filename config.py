from dotenv import load_dotenv
import os
import google.generativeai as genai  # Import Gemini SDK

# Load environment variables from .env file
load_dotenv()

# Fetch API Key securely
api_key = os.environ.get("GEMINI_KEY")

# Check if API key is loaded properly
if not api_key:
    raise ValueError("Error: GEMINI_API_KEY is not found. Please check your .env file.")

# Configure Gemini API
genai.configure(api_key=api_key)

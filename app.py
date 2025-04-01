import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image
import tempfile

# Streamlit app title
st.title("Ghibli Style Image Generator with Ghibli Diffusion")

# API Configuration (Replicate or Hugging Face)
API_URL = "https://api.replicate.com/v1/predictions"
MODEL_VERSION = "stability-ai/sd-ghibli:latest"  # Example model for Ghibli diffusion

# Get API key from secrets or user input
API_KEY = st.secrets["replicate_api_key"] if "replicate_api_key" in st.secrets else None
if not API_KEY:
    API_KEY = st.text_input("Enter your Replicate API Key:", type="password")

if API_KEY:
    HEADERS = {
        "Authorization": f"Token {API_KEY}",
        "Content-Type": "application/json"
    }

    # File uploader for user image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Open and convert uploaded image
        image = Image.open(uploaded_file).convert("RGB")
        image = image.resize((512, 512))  # Resize for compatibility
        
        # Convert image to base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode()
        
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Send request to Ghibli Diffusion API
        st.write("Generating Ghibli-style image...")
        payload = {
            "version": MODEL_VERSION,
            "input": {"image": img_b64, "prompt": "Studio Ghibli style"}
        }
        
        try:
            response = requests.post(API_URL, json=payload, headers=HEADERS)
            response.raise_for_status()
            output_url = response.json().get("output")
            
            if output_url:
                st.image(output_url, caption="Ghibli Style Image", use_container_width=True)
            else:
                st.error("Failed to generate image. Try again later.")
        
        except requests.exceptions.RequestException as e:
            st.error(f"API Error: {e}")
    else:
        st.warning("Please upload an image.")
else:
    st.warning("Please enter your Replicate API key to continue.")

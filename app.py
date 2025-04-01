import streamlit as st
import openai
from io import BytesIO
from PIL import Image
import base64

# Streamlit app title
st.title("Ghibli Style Image Generator")

# Access OpenAI API Key from Streamlit secrets
api_key = st.secrets["openai_api_key"]

# File uploader for user image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    # Generate image using OpenAI API
    st.write("Generating Ghibli-style image...")
    
    try:
        openai.api_key = api_key
        response = openai.Image.create_edit(
            image=img_str,
            prompt="Convert this image into Studio Ghibli style.",
            size="1024x1024",
            n=1
        )
        
        ghibli_image_url = response['data'][0]['url']
        st.image(ghibli_image_url, caption="Ghibli Style Image", use_column_width=True)
    
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Please upload an image.")

import streamlit as st
import openai
from io import BytesIO
from PIL import Image
import tempfile

# Streamlit app title
st.title("Ghibli Style Image Generator")

# Access OpenAI API Key from Streamlit secrets
api_key = st.secrets["openai"].get("openai_api_key", None)

if not api_key:
    st.error("API key not found. Please add it to Streamlit secrets.")
else:
    # File uploader for user image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Convert uploaded file to PNG format
        image = Image.open(uploaded_file).convert("RGBA")
        
        # Validate file size (less than 4MB)
        uploaded_file.seek(0, 2)  # Move cursor to end of file to check size
        file_size = uploaded_file.tell() / (1024 * 1024)  # Convert to MB
        uploaded_file.seek(0)  # Reset cursor position
        
        if file_size > 4:
            st.error("Uploaded image must be less than 4MB.")
        else:
            # Display the uploaded image
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            # Save image as a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                image.save(temp_file, format="PNG")
                temp_file_path = temp_file.name
            
            # Generate image using OpenAI API
            st.write("Generating Ghibli-style image...")
            
            try:
                openai.api_key = api_key
                with open(temp_file_path, "rb") as img_file:
                    response = openai.Image.create_edit(
                        image=img_file,
                        prompt="Convert this image into Studio Ghibli style.",
                        size="1024x1024",
                        n=1
                    )
                
                ghibli_image_url = response['data'][0]['url']
                st.image(ghibli_image_url, caption="Ghibli Style Image", use_container_width=True)
            
            except openai.error.InvalidRequestError as e:
                st.error("OpenAI API rejected the image. Please try a different image.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please upload an image.")

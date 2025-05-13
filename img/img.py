import openai
import streamlit as st
from PIL import Image
import io
from dotenv import load_dotenv
import os

# Set your OpenAI API key here
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# Streamlit app interface
st.title("🎨 Image Generator using DALL·E")
st.markdown("Enter a description of the image you want to generate:")

# Input field for image description
description = st.text_input("Describe the image you want to generate:")

# Button to generate image
if st.button("Generate Image"):
    if description:
        # Call OpenAI API to generate an image
        try:
            response = openai.Image.create(
                prompt=description,
                n=1,
                size="1024x1024"  # Image size can be 256x256, 512x512, or 1024x1024
            )
            image_url = response['data'][0]['url']
            st.image(image_url, caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error generating image: {e}")
    else:
        st.warning("Please enter a description.")

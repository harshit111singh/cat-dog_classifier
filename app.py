import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('cat_dog_model.keras')

model = load_model()

st.title("🐱🐶 Cat vs Dog Classifier")
st.write("Upload an image and the model will predict whether it's a cat or a dog.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # ⚠️ Match this size/preprocessing to what you used in training
    img_resized = img.resize((256, 256))
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        st.success(f"Prediction: **Dog** 🐶 (confidence: {prediction:.2%})")
    else:
        st.success(f"Prediction: **Cat** 🐱 (confidence: {(1-prediction):.2%})")
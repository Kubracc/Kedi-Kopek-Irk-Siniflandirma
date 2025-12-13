import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Kedi & Köpek Irk Analizi", page_icon="🐶")

st.title("🐱 Kedi ve Köpek Irk Sınıflandırma 🐶")
st.write("Bir kedi veya köpek fotoğrafı yükleyin, yapay zeka ırkını tahmin etsin!")

# --- MODELİ YÜKLEME (Önbelleğe alıyoruz ki hızlı çalışsın) ---
@st.cache_resource
def get_model():
    model = load_model("keras_model.h5", compile=False)
    return model

@st.cache_resource
def get_labels():
    with open("labels.txt", "r", encoding="utf-8") as f:
        class_names = f.readlines()
    return class_names

# Yükleme mesajı
with st.spinner('Yapay zeka modeli yükleniyor...'):
    model = get_model()
    class_names = get_labels()

# --- RESİM YÜKLEME ALANI ---
uploaded_file = st.file_uploader("Lütfen bir resim seçin...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Resmi ekranda göster
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Yüklenen Resim', use_container_width=True)
    
    st.write("")
    st.write("🔍 **Analiz ediliyor...**")

    # --- TAHMİN İŞLEMİ ---
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # --- SONUCU GÖSTER ---
    st.success(f"Sonuç: **{class_name.strip()[2:]}**")
    st.info(f"Doğruluk Oranı: %{confidence_score * 100:.2f}")

    # İsteğe bağlı: Grafiksel çubuk (progress bar)
    st.progress(int(confidence_score * 100))
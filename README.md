# 🐱🐶 Kedi ve Köpek Irk Sınıflandırma Sistemi (Deep Learning)

Bu proje, Derin Öğrenme (Deep Learning) teknikleri kullanılarak kedi ve köpeklerin farklı ırklarını fotoğraflardan tespit etmek amacıyla geliştirilmiştir. Kullanıcı dostu ve etkileşimli bir deneyim sunmak için **Streamlit** kütüphanesi kullanılarak modern bir web arayüzü tasarlanmıştır.

## 🎯 Proje Amacı
Projenin temel amacı, kullanıcı tarafından sisteme yüklenen bir kedi veya köpek fotoğrafını analiz ederek, modelin daha önceden öğrendiği **35 farklı ırk** özelliklerine göre sınıflandırma yapması ve sonucu güven oranıyla (confidence score) birlikte göstermesidir.

## 🚀 Özellikler
* **Geniş Veri Seti:** 7.000+ adet görüntü ile eğitilmiş model.
* **Transfer Learning:** Google MobileNet mimarisi üzerinde Fine-tuning yapılmıştır.
* **Web Arayüzü:** Streamlit ile geliştirilmiş kolay kullanımlı arayüz.
* **Hızlı Tahmin:** Saniyeler içerisinde ırk tespiti.

## 🛠 Kullanılan Teknolojiler
Bu projede aşağıdaki açık kaynaklı teknolojiler kullanılmıştır:
* **Dil:** Python 3.10
* **Yapay Zeka:** TensorFlow / Keras (v2.15)
* **Arayüz:** Streamlit
* **Görüntü İşleme:** Pillow (PIL) & NumPy

## 💻 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. **Projeyi indirin:**
   GitHub sayfasından projeyi zip olarak indirin veya klonlayın.

2. **Gerekli kütüphaneleri yükleyin:**
   Proje dizininde terminali açarak şu komutu çalıştırın:
   ```bash
   pip install -r requirements.txt

3.Uygulamayı başlatın: Kurulum tamamlandıktan sonra aşağıdaki komutla arayüzü açabilirsiniz:
streamlit run main.py



🎓 Ders Atıfı
Bu proje, İskenderun Teknik Üniversitesi (İSTE) Mühendislik ve Doğa Bilimleri Fakültesi,MÜHENDİSLİKTE BİLGİSAYAR UYGULAMALARI dersi kapsamında, Dr. Öğr. Üyesi H. İbrahim OKUR danışmanlığında geliştirilmiştir.

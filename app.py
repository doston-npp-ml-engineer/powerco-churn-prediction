import streamlit as st

st.set_page_config(
    page_title="PowerCo Churn Prediction",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ PowerCo — Mijozlar Churn Bashorati")

st.markdown("""
Ushbu loyiha **energiya kompaniyasi (PowerCo)** mijozlarining yaqin kelajakda 
xizmatdan voz kechish (churn) ehtimolini **XGBoost** algoritmi yordamida bashorat qiladi.

### 📌 Loyiha haqida qisqacha
- **Dataset:** 14,606 ta mijoz, 30+ xususiyat (iste'mol, marja, xizmat turi va h.k.)
- **Muammo:** disbalanslashgan dataset (mijozlarning atigi 9.7%i churn qiladi)
- **Yechim:** scale_pos_weight, regularizatsiya va cross-validation orqali ishonchli model qurish

### 🧭 Navigatsiya
Chap tomondagi menyudan quyidagi sahifalarga o'ting:
- **📊 Ma'lumotlar tahlili** — dataset haqida statistika va grafiklar
- **🔮 Bashorat** — yangi mijoz ma'lumotlarini kiritib, churn ehtimolini bilib oling
- **ℹ️ Loyiha haqida** — metodologiya va yakuniy natijalar
""")

st.info("👈 Boshlash uchun chap tomondagi menyudan sahifa tanlang")
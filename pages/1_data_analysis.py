import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ma'lumotlar tahlili", page_icon="📊")
st.title("📊 Dataset Tahlili")

st.markdown("""
### PowerCo mijozlar dataseti
- **14,606 ta mijoz**, 26 ta original xususiyat (encoding'dan keyin 30 taga yetdi)
- **Manba:** Kaggle — PowerCo customer churn (BCG loyihasi asosida)
""")

st.subheader("⚖️ Churn balansi")

col1, col2 = st.columns(2)
with col1:
    st.metric("Qolib qoluvchi mijozlar (churn=0)", "90.28%")
with col2:
    st.metric("Ketib qoluvchi mijozlar (churn=1)", "9.72%")

st.warning("⚠️ Bu — kuchli disbalanslashgan dataset. Shuning uchun oddiy Accuracy metrikasi yetarli emas, F1-score va ROC-AUC ustuvor metrikalar sifatida ishlatildi.")

st.subheader("🏆 Eng muhim 5 ta belgi")

importance_data = pd.DataFrame({
    'Belgi': ['margin_net_pow_ele', 'origin_up (kampaniya 1)', 'origin_up (kampaniya 2)', 'has_gas', 'forecast_discount_energy'],
    'Muhimlik': [0.081, 0.068, 0.065, 0.055, 0.048]
})

st.bar_chart(importance_data.set_index('Belgi'))

st.markdown("""
**Izoh:**
- **margin_net_pow_ele** — elektr quvvatidan olinadigan sof marja, eng kuchli signal
- **origin_up** — mijoz qaysi kampaniya orqali qo'shilgani, sodiqlik darajasi bilan bog'liq
- **has_gas** — bir nechta xizmatdan foydalanuvchi mijozlar odatda ko'proq "bog'langan"
- **forecast_discount_energy** — chegirma miqdori, narx sezgirligini aks ettiradi
""")
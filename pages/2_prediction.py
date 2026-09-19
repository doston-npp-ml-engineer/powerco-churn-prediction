import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb

st.set_page_config(page_title="Bashorat", page_icon="🔮")
st.title("🔮 Mijoz Churn Bashorati")

# Saqlab qo'ygan model va ustunlar ro'yxatini yuklaymiz
model = xgb.XGBClassifier()
model.load_model('churn_model.json')
feature_columns = joblib.load('feature_columns.pkl')

st.markdown("Quyida mijoz haqidagi ma'lumotlarni kiriting, model uning ketib qolish ehtimolini bashorat qiladi.")

st.subheader("📋 Mijoz ma'lumotlarini kiriting")

col1, col2 = st.columns(2)

with col1:
    cons_12m = st.number_input("Yillik elektr iste'moli (kWh)", min_value=0, value=2000)
    num_years_antig = st.number_input("Necha yildan buyon mijoz", min_value=0, max_value=30, value=5)
    nb_prod_act = st.number_input("Faol mahsulotlar soni", min_value=0, max_value=10, value=1)
    net_margin = st.number_input("Sof marja", value=200.0)

with col2:
    margin_net_pow_ele = st.number_input("Elektr quvvatidan sof marja", value=25.0)
    pow_max = st.number_input("Maksimal quvvat (kW)", min_value=0.0, value=15.0)
    forecast_discount_energy = st.number_input("Prognoz chegirma", min_value=0.0, value=0.0)
    has_gas = st.selectbox("Gaz xizmati bormi?", ["Yo'q", "Ha"])

st.subheader("🏷️ Kategoriyalar")
col3, col4 = st.columns(2)

with col3:
    origin_up = st.selectbox(
        "Kelib chiqish kampaniyasi",
        ["lxidpiddsbxsbosboudacockeimpuepw", "kamkkxfxxuwbdslkwifmmcsiusiuosws",
         "ldkssxwpmemidmecebumciepifcamkci", "usapbepcfoloekilkwsdiboslwaxobdp",
         "ewxeelcelemmiwuafmddpobolfuxioce"]
    )

with col4:
    channel_sales = st.selectbox(
        "Savdo kanali",
        ["foosdfpfkusacimwkcsosbicdxkicaua", "lmkebamcaaclubfxadlmueccxoimlema",
         "usilxuppasemubllopkaafesmlibmsdf", "ewpakwlliwisiwduibdlfmalxowmwpci",
         "sddiedcslfslkckwlfkdpoeeailfpeds", "epumfxlbckeskwekxbiuasklxalciiuu",
         "fixdbufsefwooaasfcxdxadsiekoceaa", "MISSING"]
    )

st.divider()

if st.button("🔮 Bashorat qilish", type="primary"):

    # 1. Barcha ustunlar uchun bo'sh (0) qator tayyorlaymiz
    input_data = {col: 0 for col in feature_columns}

    # 2. Foydalanuvchi kiritgan qiymatlarni joylaymiz
    input_data['cons_12m'] = cons_12m
    input_data['num_years_antig'] = num_years_antig
    input_data['nb_prod_act'] = nb_prod_act
    input_data['net_margin'] = net_margin
    input_data['margin_net_pow_ele'] = margin_net_pow_ele
    input_data['margin_gross_pow_ele'] = margin_net_pow_ele
    input_data['pow_max'] = pow_max
    input_data['forecast_discount_energy'] = forecast_discount_energy
    input_data['has_gas'] = 1 if has_gas == "Ha" else 0

    # 3. Kategorik ustunlarni One-Hot formatga o'tkazamiz
    origin_col = f"origin_up_{origin_up}"
    if origin_col in input_data:
        input_data[origin_col] = 1

    channel_col = f"channel_sales_{channel_sales}"
    if channel_col in input_data:
        input_data[channel_col] = 1

    # 4. Dictionary'ni model tushunadigan DataFrame'ga aylantiramiz
    input_df = pd.DataFrame([input_data])[feature_columns]

    # 5. Bashorat qilamiz
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # 6. Natijani ko'rsatamiz
    st.subheader("📊 Natija")

    if prediction == 1:
        st.error(f"⚠️ Bu mijoz **ketib qolish** ehtimoli yuqori: **{probability:.1%}**")
    else:
        st.success(f"✅ Bu mijoz **qolib ketish** ehtimoli yuqori (churn ehtimoli: {probability:.1%})")

    st.progress(float(probability))
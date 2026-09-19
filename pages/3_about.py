import streamlit as st

st.set_page_config(page_title="Loyiha haqida", page_icon="ℹ️")
st.title("ℹ️ Loyiha haqida")

st.markdown("""
## 🎯 Maqsad

Energiya kompaniyasi (**PowerCo**) mijozlarining yaqin kelajakda xizmatdan voz kechish 
(**churn**) ehtimolini oldindan bashorat qilish — bu kompaniyaga xavf ostidagi mijozlarni 
erta aniqlab, ular bilan ishlashga (chegirma, individual taklif) imkon beradi.

## 🛠️ Ishlatilgan usullar

1. **Ma'lumotni tayyorlash** — kategorik ustunlarni One-Hot Encoding bilan kodlash
2. **Bazaviy model** — default parametrlar bilan XGBClassifier (F1=0.15)
3. **GridSearchCV** — n_estimators, learning_rate, max_depth kombinatsiyalarini sozlash
4. **scale_pos_weight** — disbalansni (9.7% churn) hisobga olib, Recall'ni oshirish
5. **Regularizatsiya** — gamma, reg_alpha, reg_lambda bilan overfitting'ni kamaytirish
6. **Cross-validation** — 5-fold orqali natijaning barqarorligini tasdiqlash

## 📊 Yakuniy natijalar

| Metrika | Qiymat |
|---|---|
| Cross-validation F1 (o'rtacha) | 0.26 |
| ROC-AUC | 0.68 |
| Recall (churn'ni topish darajasi) | 0.31 |

## 💡 Asosiy xulosa

Disbalanslashgan datasetlarda oddiy Accuracy metrikasiga ishonib bo'lmaydi — 90% 
accuracy ko'rsatgan bazaviy model, aslida ketib qoluvchi mijozlarning atigi 9%ini 
topa olgan. `scale_pos_weight` va to'g'ri metrikalar (F1, Recall, ROC-AUC) tanlash 
orqali, model amaliy jihatdan foydali darajaga yetkazildi.

## 👤 Muallif

Ushbu loyiha Najot Ta'lim Machine Learning kursi doirasida, energetika sohasiga 
moslashtirilgan holda bajarildi.

**GitHub:** [doston-npp-ml-engineer/powerco-churn-prediction](https://github.com/doston-npp-ml-engineer/powerco-churn-prediction)
""")
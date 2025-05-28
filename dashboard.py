
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Bank Al Wahda – Executive AI Dashboard")

df = pd.read_excel("Bank_AlWahda_Data.xlsx")

st.subheader("📊 Key Branch Metrics")
st.dataframe(df)

st.subheader("🔍 Fraud Detection Alerts")
suspicious = df[df["العمليات المشبوهة"] > 4]
st.table(suspicious[["الفرع", "العمليات المشبوهة"]])

st.subheader("🧠 AI Recommendation Example")
st.success("فرع سبها يحتاج إلى مراجعة فورية لزيادة عدد الشكاوى وانخفاض الأداء.")

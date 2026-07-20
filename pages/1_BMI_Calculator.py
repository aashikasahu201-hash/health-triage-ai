import streamlit as st
from sidebar_ui import render_sidebar
from translations import t

st.set_page_config(page_title="BMI Calculator", page_icon="\u2696\uFE0F")
render_sidebar()
lang = st.session_state.get("output_lang", "en")

st.title(f"\u2696\uFE0F {t('bmi_title', lang)}")
st.divider()

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input(f"\u2696\uFE0F {t('weight', lang)}", min_value=1.0, max_value=300.0, value=60.0, step=0.5)
with col2:
    height = st.number_input(f"\U0001F4CF {t('height', lang)}", min_value=50.0, max_value=250.0, value=165.0, step=0.5)

if st.button(f"\U0001F9EE {t('calculate_bmi', lang)}", type="primary"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        category, emoji = "Underweight", "\U0001F7E1"
    elif bmi < 25:
        category, emoji = "Normal weight", "\U0001F7E2"
    elif bmi < 30:
        category, emoji = "Overweight", "\U0001F7E0"
    else:
        category, emoji = "Obese", "\U0001F534"
    st.metric("BMI", f"{bmi:.1f}", f"{emoji} {category}")

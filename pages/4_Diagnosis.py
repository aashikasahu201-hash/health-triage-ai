import streamlit as st
import pandas as pd
from sidebar_ui import render_sidebar
from doctor_recommendation import get_doctor
from diet_exercise import get_diet_exercise
from translations import t
from translate_output import translate_output

st.set_page_config(page_title="Diagnosis", page_icon="\U0001F52C")
render_sidebar()
lang = st.session_state.get("output_lang", "en")

st.title(f"\U0001F52C {t('diagnosis_title', lang)}")
st.divider()

if "last_entry" not in st.session_state:
    st.info("No check completed yet. Go to the Symptom Checker page first.")
else:
    entry = st.session_state.last_entry
    condition = entry.get("condition")

    if not condition:
        st.warning("Your last check was flagged as an emergency \u2014 no condition prediction was made. Please seek immediate care.")
    else:
        desc_df = pd.read_csv("data/symptom_Description.csv")
        prec_df = pd.read_csv("data/symptom_precaution.csv")

        st.subheader(f"{t('predicted_condition', lang)}: {condition}")
        c1, c2 = st.columns(2)
        c1.metric(t("confidence", lang), f"{entry.get('confidence', 0)*100:.0f}%")
        c2.metric(f"\U0001FA7A {t('specialist', lang)}", get_doctor(condition))

        st.write(f"**{t('about_condition', lang)}:**")
        desc_row = desc_df[desc_df["Disease"].str.strip() == condition.strip()]
        desc_text = desc_row.iloc[0]["Description"] if not desc_row.empty else "No description available."
        st.write(translate_output(desc_text, lang))

        st.write(f"**{t('precautions', lang)}:**")
        prec_row = prec_df[prec_df["Disease"].str.strip() == condition.strip()]
        if not prec_row.empty:
            for c in ["Precaution_1", "Precaution_2", "Precaution_3", "Precaution_4"]:
                val = prec_row.iloc[0][c]
                if pd.notna(val):
                    st.write(f"- {translate_output(val, lang)}")

        tips = get_diet_exercise(condition)
        st.write(f"**\U0001F957 {t('diet_tips', lang)}:**")
        st.info(translate_output(tips["diet"], lang))
        st.write(f"**\U0001F3C3 {t('exercise_tips', lang)}:**")
        st.info(translate_output(tips["exercise"], lang))

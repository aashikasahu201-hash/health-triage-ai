import streamlit as st
import pandas as pd
from collections import Counter
from sidebar_ui import render_sidebar
from translations import t

st.set_page_config(page_title="Dashboard", page_icon="\U0001F4CA")
render_sidebar()
lang = st.session_state.get("output_lang", "en")

st.title(f"\U0001F4CA {t('dashboard_title', lang)}")
st.divider()

if "history" not in st.session_state or not st.session_state.history:
    st.info(f"\U0001F4ED {t('no_data', lang)}")
else:
    hist_df = pd.DataFrame(st.session_state.history)

    col1, col2, col3 = st.columns(3)
    col1.metric(f"\U0001F9EE {t('total_checks', lang)}", len(hist_df))
    col2.metric(f"\U0001F6A8 {t('emergency_flags', lang)}", int((hist_df["severity"] == "Emergency").sum()))
    col3.metric(f"\U0001FA7A {t('unique_conditions', lang)}", hist_df["condition"].nunique())

    st.bar_chart(hist_df["severity"].value_counts())

    all_reported = [s for symptoms in hist_df["symptoms"] for s in symptoms]
    symptom_counts = pd.Series(Counter(all_reported)).sort_values(ascending=False).head(10)
    st.bar_chart(symptom_counts)

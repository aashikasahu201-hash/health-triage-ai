import streamlit as st
from sidebar_ui import render_sidebar
from translations import t

st.set_page_config(page_title="Patient History", page_icon="\U0001F4DD")
render_sidebar()
lang = st.session_state.get("output_lang", "en")

SEVERITY_EMOJI = {
    "Emergency": "\U0001F534",
    "See doctor soon": "\U0001F7E1",
    "Self-care with monitoring": "\U0001F7E2",
}

st.title(f"\U0001F4DD {t('history_title', lang)}")
st.divider()

if "history" not in st.session_state or not st.session_state.history:
    st.info(f"\U0001F4ED {t('no_checks', lang)}")
else:
    for entry in reversed(st.session_state.history):
        emoji = SEVERITY_EMOJI.get(entry["severity"], "\u26AA")
        with st.expander(f"{emoji} {entry['timestamp']} \u2014 {entry['severity']}"):
            st.write(f"\U0001FA7A **Symptoms:** {', '.join(entry['symptoms'])}")
            if entry.get("condition"):
                st.write(f"\U0001F52C **Condition:** {entry['condition']} ({entry.get('confidence', 0)*100:.0f}% confidence)")
    if st.button(f"\U0001F5D1\uFE0F {t('clear_history', lang)}"):
        st.session_state.history = []
        st.rerun()

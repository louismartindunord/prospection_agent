import streamlit as st
from utils.user_infos_form_state import get_user_information


def save_user_infos_in_session_state(user_id=1):
    if "user_infos" not in st.session_state:
        st.session_state["user_infos"] = get_user_information(user_id)

import streamlit as st
from utils.user_infos_form_state import display_missing_users_infos


def main():
    st.set_page_config(page_title="Dashboard", page_icon="📊")
    st.title(" 📊 Dashboard")
    display_missing_users_infos()


if __name__ == "__main__":
    main()

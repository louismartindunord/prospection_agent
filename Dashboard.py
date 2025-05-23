import streamlit as st
from utils.user_infos_form_state import display_missing_users_infos
from utils.session_state_management import save_user_infos_in_session_state


def main():
    save_user_infos_in_session_state()
    st.set_page_config(page_title="Dashboard", page_icon="📊")
    st.title(" 📊 Dashboard")
    # display_missing_users_infos(user_id=st.session_state["user_infos"].get("user_id"))


if __name__ == "__main__":
    main()

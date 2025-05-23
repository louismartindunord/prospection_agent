import streamlit as st
from utils.user_infos_form_state import (
    is_user_information_form_active,
    close_user_information_form,
    check_email,
    check_openai_key,
    save_user_informations,
    get_user_information,
)

from forms.user_infos_page_form import (
    display_user_personnal_info_form,
    display_user_personnal_info,
)

from utils.connection import insert_key_in_env_file, verify_presence_of_api_key


def main():
    user_infos = st.session_state["user_infos"]

    if is_user_information_form_active():
        display_user_personnal_info_form(user_infos=user_infos)
    else:
        display_user_personnal_info(user_infos=user_infos)

        # Compagny activity


if __name__ == "__main__":
    main()

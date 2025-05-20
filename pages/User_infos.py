import streamlit as st
from utils.user_infos_form_state import (
    is_user_information_form_active,
    close_user_information_form,
    check_email,
    check_openai_key,
    save_user_informations,
    get_user_information,
)

from utils.connection import insert_key_in_env_file, verify_presence_of_api_key


def main():
    user_infos = get_user_information()
    print(user_infos)
    if is_user_information_form_active():
        with st.form("user_informations_form"):
            firstname = st.text_input(label="Firsname", value=user_infos["firstname"])
            lastname = st.text_input(label="Lastname", value=user_infos["lastname"])
            email = st.text_input("Email", value=user_infos["email"])
            openai_api_key = st.text_input(
                "your Openai Api key", type="password", value="****"
            )
            (
                col1,
                col2,
            ) = st.columns(2)

            with col1:
                submit_user_information_form = st.form_submit_button("submit")
            with col2:
                close_user_information_button = st.form_submit_button("Close")
            if close_user_information_button:
                close_user_information_form()

            if submit_user_information_form:
                validate_all_information = []
                email, validate_email = check_email(email=email)
                if validate_email:
                    validate_all_information.append(True)
                else:
                    st.error(
                        "Something went wrong, may be your email isn't is the right format"
                    )
                if check_openai_key(open_ai_key=openai_api_key) is None:
                    st.error("Your Openai api is not be valide")
                else:
                    validate_all_information.append(True)

                if all(validate_all_information) == True:
                    save_user_informations(firstname, lastname, email)
                    insert_key_in_env_file(
                        key_name="OPENAI_API_KEY", key_value=openai_api_key
                    )

    else:

        # Personnal infos part
        st.divider()
        st.title("Your personal infos :")
        st.write(f"Firstname : {user_infos["firstname"]}")
        st.write(f"Lastname : {user_infos["lastname"]}")
        st.write(f"Email : {user_infos["email"]}")

        if verify_presence_of_api_key("OPENAI_API_KEY"):
            st.success("your OPENAI_API_KEY is saved")
        else:
            st.error("OPENAI_API_KEY is not saved yes")

        if st.button("Modify"):
            st.session_state["user_information_form_active"] = True
            st.rerun()

        st.divider()

        # Compagny activity


if __name__ == "__main__":
    main()

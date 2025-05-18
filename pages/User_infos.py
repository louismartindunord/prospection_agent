import streamlit as st
from utils.user_infos_form_state import (
    is_user_information_form_active,
    close_user_information_form,
    check_email,
    check_openai_key,
    save_user_informations,
    get_user_information,
)


def main():
    user_infos = get_user_information()
    if is_user_information_form_active():
        with st.form("user_informations_form"):
            firstname = st.text_input(label="Firsname")
            lastname = st.text_input(label="Lastname")
            email = st.text_input("email")
            openai_api_key = st.text_input("your Openai Api key", type="password")

            submit_user_information_form = st.form_submit_button("submit")
            close_user_information_button = st.form_submit_button("Close")
            if close_user_information_button:
                close_user_information_form()

            if submit_user_information_form:
                validate_all_information = []
                email, validate_email = check_email(email=email)
                if validate_email:
                    st.success("Everything is ok here !")
                    validate_all_information.append(True)
                else:
                    st.error(
                        "Something went wrong, may be your email isn't is the right format"
                    )
                if check_openai_key() is None:
                    st.error("Your Openai api is not be valide")
                else:
                    validate_all_information.append(True)

                if all(validate_all_information) == True:
                    save_user_informations(firstname, lastname, email)
    else:
        st.write(f"Firstname : {user_infos["firstname"]}")
        st.write(f"Lastname : {user_infos["lastname"]}")
        st.write(f"email : {user_infos["email"]}")
        if st.button("Modify"):
            st.session_state["user_information_form_active"] = True
            st.rerun()


if __name__ == "__main__":
    main()

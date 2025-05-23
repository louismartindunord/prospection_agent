import streamlit as st
from email_validator import validate_email, EmailNotValidError
from utils.connection import create_connection, return_api_key
import openai
import sqlite3


# Check if the user information form is active
def is_user_information_form_active():
    if (
        "user_information_form_active" in st.session_state.keys()
        and st.session_state["user_information_form_active"]
    ):
        return True
    else:
        return False


def close_user_information_form():
    st.session_state["user_information_form_active"] = None
    st.rerun()


def return_missing_users_infos_in_systeme(user_id):
    user_infos = get_user_information(user_id)
    user_infos["api_key"] = return_api_key("OPENAI_API_KEY")
    missing_infos = []
    for key, value in user_infos.items():
        if value is None:
            missing_infos.append({key: value})
    return missing_infos


def display_missing_users_infos(user_id):
    missing_infos = return_missing_users_infos_in_systeme(user_id)
    if len(missing_infos) > 0:
        st.page_link(
            "pages/User_infos.py",
            label="Veuillez remplir vos informations personelles  ",
        )


# { k for k, v in missing_infos})


# close the form when the close button is click


def check_email(email: str) -> bool:
    try:
        emailinfo = validate_email(email, check_deliverability=False)
        email = emailinfo.normalized
        email_validate = True
        return email, email_validate

    except EmailNotValidError as e:
        email_validate = False
        return e, email_validate


def check_openai_key(open_ai_key: str) -> bool:
    client = openai.OpenAI(api_key=open_ai_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True


def save_user_informations(
    id: int,
    firstname: str,
    lastname: str,
    email: str,
    compagny_type: str,
    activity: str,
    activity_large_description: str,
):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        with open("sql/update_user_infos.sql", "r") as f:
            sql = f.read()
        cursor.execute(
            sql,
            (
                firstname,
                lastname,
                email,
                compagny_type,
                activity,
                activity_large_description,
                id,
            ),
        )
        conn.commit()
        st.success("Your personnal informations are saved in database")
        return True
    except sqlite3.OperationalError as error:
        print(f"erreur lors de la sauvegarde des informations utilisateurs {error}")
        return False
    finally:
        cursor.close()
        conn.close()


def get_user_information(user_id: int):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        with open("sql/get_user_informations.sql", "r") as f:
            sql = f.read()
        cursor.execute(sql, (user_id,))
        row = cursor.fetchall()
        if not row:
            print(f"Aucun utilisateur trouvé avec l'ID {user_id}")
            return {
                "id": None,
                "firstname": None,
                "lastname": None,
                "email": None,
                "compagny_type": None,
                "compagny_activity": None,
                "compagny_large_activity": None,
            }

        data = [element for elements in row for element in elements]
        user_infos = {
            "id": data[0],
            "firstname": data[1],
            "lastname": data[2],
            "email": data[3],
            "compagny_type": data[4],
            "compagny_activity": data[5],
            "compagny_large_activity": data[6],
        }
        return user_infos

    except sqlite3.OperationalError as error:
        print(f"Erreur lors de la récupération des informations utilisateur : {error}")
        return {"id": None, "firstname": None, "lastname": None, "email": None}

    finally:
        cursor.close()
        conn.close()

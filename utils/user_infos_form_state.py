import streamlit as st
from email_validator import validate_email, EmailNotValidError
from utils.connection import create_connection
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


# close the form when the close button is click
def close_user_information_form():
    st.session_state["user_information_form_active"] = None
    st.rerun()


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


def save_user_informations(firstname: str, lastname: str, email: str):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        with open("sql/save_user_informations.sql", "r") as f:
            sql = f.read()
        cursor.execute(sql, (firstname, lastname, email))
        return True
    except sqlite3.OperationalError as error:
        print(f"erreur lors de la sauvegarde des informations utilisateurs {error}")
        return False
    finally:
        cursor.close()
        conn.close()


def get_user_information():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        with open("sql/get_user_informations.sql", "r") as f:
            sql = f.read()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row
    except sqlite3.OperationalError as error:
        print(f"erreur lors de la récuperation des informations utilisateur {error}")

    finally:
        cursor.close()
        conn.close()

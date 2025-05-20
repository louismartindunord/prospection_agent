import sqlite3
from dotenv import load_dotenv, unset_key, set_key
from sqlalchemy import null
import streamlit as st
import os


def create_connection():
    try:
        conn = sqlite3.connect("Prospection.db")
        return conn
    except sqlite3.OperationalError as error:
        print(f"impossible de se connecter à la base de donnée  erreur {error}")


def insert_key_in_env_file(key_name: str, key_value: str):
    try:
        set_key(".env", key_name, key_value)
        st.success("La clé est sauvegardé dans vos variable")
    except:
        st.error("Erreur lors de la sauvegarde de la clée")


def verify_presence_of_api_key(key_name):
    load_dotenv()
    if os.getenv(key_name) is not null:
        return True
    else:
        return False


def return_api_key(key_name):
    load_dotenv()
    return os.getenv(key_name)


def modify_key():
    pass

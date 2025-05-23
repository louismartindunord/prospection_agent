import pandas as pd
import sqlite3
import streamlit as st

from utils.connection import create_connection


def initialize_campagne_form_session_state():
    if not "campagne_form_session_state" in st.session_state:
        st.session_state["campagne_form_session_state"] = "all_campagnes_presentation"


def modify_campagne_form_session_state(status: str):
    # initialisation de la st.session_state avant de lui mettre une value
    if not "campagne_form_session_state" in st.session_state:
        st.session_state["campagne_form_session_state"] = "all_campagnes_presentation"
    if status:
        st.session_state["campagne_form_session_state"] = "campagne_with_ia"
    else:
        st.session_state["campagne_form_session_state"] = "classique_campagne"
    st.rerun()


def get_user_campagne(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        with open("sql/get_campagne_for_user.sql", "r") as f:
            cursor.execute(f.read(), (user_id,))
            data = cursor.fetchall()
        df = pd.DataFrame(data, columns=["id", "name", "start_date", "end_date"])
        return df

    except sqlite3.OperationalError as error:
        print(f"Erreur lors de la récupération des campagne : {error}")
        df = pd.DataFrame(
            {"id": [None], "name": [None], "start_date": [None], "end_date": [None]}
        )
        return df
    finally:
        cursor.close()
        conn.close()

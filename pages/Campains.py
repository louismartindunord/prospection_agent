import streamlit as st
from utils.session_state_management import save_user_infos_in_session_state
from utils.user_campagne import (
    get_user_campagne,
    modify_campagne_form_session_state,
    initialize_campagne_form_session_state,
)

from agents.find_compagny_for_activity import (
    agent_to_find_market_of_activity,
    transform_agent_to_find_market_output_into_editable_df,
)


def main():
    save_user_infos_in_session_state()
    initialize_campagne_form_session_state()

    if st.session_state["campagne_form_session_state"] == "all_campagnes_presentation":
        all_campagne = get_user_campagne(st.session_state["user_infos"].get("id"))
        st.write(all_campagne)

    if st.session_state["campagne_form_session_state"] == "campagne_with_ia":
        df = transform_agent_to_find_market_output_into_editable_df()
        # response = agent_to_find_market_of_activity()
        st.data_editor(df)

    if st.button("Nouvelle campagne IA"):
        modify_campagne_form_session_state(status="campagne_with_ia")
    if st.button("Nouvelle campagne"):
        modify_campagne_form_session_state(status="classique_campagne")


if __name__ == "__main__":
    main()

import langchain
import streamlit as st
from agents.agent_parser.find_compagny_type_parser import society_type_parser
from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.runnables import RunnableLambda


import os
from dotenv import load_dotenv

load_dotenv()


def pydantic_list_to_dicts(pydantic_model):
    return [item.model_dump() for item in pydantic_model.companies]


def agent_to_find_market_of_activity():
    user_infos = st.session_state["user_infos"]

    prompt = """Je suis {work_description}, je cherche à identifier mon client idéal.
    
    Peux-tu me proposer une liste d'entreprises types (secteur, taille et modèle économique) qui auraient un intérêt stratégique à faire appel à mes services ?
    
    Pour chaque type, précise les **postes décisionnaires** typiques.
    
    Je suis en phase de test donc propose que 2 liste d'entreprise types
    
    {format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["work_description"],
        template=prompt,
        partial_variables={
            "format_instructions": society_type_parser.get_format_instructions()
        },
    )

    os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")
    llm = ChatMistralAI(
        model="mistral-large-latest",
        temperature=0,
        max_retries=2,
    )

    actity_infos = user_infos.get("activity")

    chain = (
        summary_prompt_template
        | llm
        | society_type_parser
        | RunnableLambda(pydantic_list_to_dicts)
    )

    res = chain.invoke({"work_description": actity_infos})
    print(res[0])
    print(res[1])
    # print(f"le type de  res.companies :{type(res.companies)} ")
    # print(f"le nombre d'element res.companies :{len(res.companies)} ")
    return res



 def transform_agent_to_find_market_output_into_editable_df():
    compagnies = agent_to_find_market_of_activity()
    #


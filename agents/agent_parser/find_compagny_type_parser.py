from typing import List, Dict
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class SocietyTypeParser(BaseModel):
    society: str = Field(description="The name of the society")
    number_of_employe: int = Field(description="The size of the company")
    business_model_type: str = Field(
        description="The type of the company: Start-up, PME, Group, etc."
    )
    decision_makers: List[str] = Field(
        description="List of typical decision-maker job titles for this type"
    )


class SocietyTypeListParser(BaseModel):
    companies: List[SocietyTypeParser]


society_type_parser = PydanticOutputParser(pydantic_object=SocietyTypeListParser)

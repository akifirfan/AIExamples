from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
load_dotenv()

# Init Groq Model
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7
    )

def str_output_parser():
    # prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Tell the joke about the following subject."),
            ("human","{input}")
        ]
    )

    parser = StrOutputParser() 
    
    # Create LLM Chain 
    chain = prompt | llm | parser

    return chain.invoke({"input": "Dog"})

def list_output_parser():
    # prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Generate a 10 synonyms of following word and return a comma separated list."),
            ("human","{input}")
        ]
    )

    parser = CommaSeparatedListOutputParser() 
    
    # Create LLM Chain 
    chain = prompt | llm | parser

    return chain.invoke({"input": "Candid"})

def json_output_parser():
    prompt = ChatPromptTemplate.from_messages({
        ("system","Extract information from the following phrase. Formating instructions {format_instruction}"),
        ("human", "{input}")
    })

    
    class Person(BaseModel):
        name: str = Field(description="The name of recipe")
        ingredients: list = Field(description="The ingredeients of recipe")


    parser = JsonOutputParser(pydantic_object= Person)

    chain = prompt | llm | parser

    return chain.invoke(
        {
            "input": "Coffee ingredients are Sugar, Milk, Coffee",
            "format_instruction": parser.get_format_instructions()
        }
    )

print(json_output_parser())
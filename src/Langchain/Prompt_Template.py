from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Init Groq Model
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=1
    )

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are IELTS guider, help the students to upskill about given module."),
        ("human","{input}")
    ]
)
# Create LLM Chain 
chain = prompt | llm

response = chain.invoke({"input": "Reading"})

print(response.content)
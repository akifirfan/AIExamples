from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=1
    )

response = llm.stream("Hi, write a poem about AI")

for chunk in response:
    print(chunk.content)
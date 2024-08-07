
import langchain
import os
import getpass

os.environ["GROQ_API_KEY"] = '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' #getpass.getpass() # 'AIzaSyBzDx7JnbfcGZfwqVqNhaUjh8MvjmLo_MY' #

print('The key is! ' + os.environ["GROQ_API_KEY"]) 

from langchain_groq import ChatGroq

model = ChatGroq(model="llama3-8b-8192")

from langchain_core.messages import HumanMessage, SystemMessage


from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "italian", "text": "hi"})

#print(result)

#print(result.to_messages())

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = prompt_template | model | parser

chain.invoke({"language": "Italian", "text": "hi"})

print(chain)
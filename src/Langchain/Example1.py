import langchain
import os
import getpass

os.environ["GROQ_API_KEY"] = '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' #getpass.getpass() # 'AIzaSyBzDx7JnbfcGZfwqVqNhaUjh8MvjmLo_MY' #

print('The key is! ' + os.environ["GROQ_API_KEY"]) 

from langchain_groq import ChatGroq

model = ChatGroq(model="llama3-8b-8192")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate following message from English to Italian"),
    HumanMessage(content="Hi! I Hope you are doing well.")
]

result = model.invoke(messages)
print(result)
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
p = parser.invoke(result)

print(p)
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
import bs4 #import BeautifulSoup
load_dotenv()

def web_document_loader(url):
    # web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/"),
    # bs_kwargs=dict(
    #     parse_only=bs4.SoupStrainer(
    #         class_=("post-content", "post-title", "post-header")
    #     )
    # ),
    loader = WebBaseLoader(
        web_paths = (url,),
        bs_kwargs = dict(
            parse_only = bs4.SoupStrainer(
                class_ = ("anchor anchorWithStickyNavbar_LWe7")
            )
        )
    )
    docs = loader.load()
    return docs

docs = web_document_loader('https://python.langchain.com/v0.2/docs/concepts/')

#print(docs)

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.4
)

prompt = ChatPromptTemplate.from_template("""
    Answer the user's questions:
    Context: {context}
    Question: {input}                                      
""")

#chain = prompt | llm
chain = create_stuff_documents_chain(
    llm = llm,
    prompt = prompt
)
response = chain.invoke(
    {"input":"What is LCEL?",
     "context": docs
     }
)

print(response)
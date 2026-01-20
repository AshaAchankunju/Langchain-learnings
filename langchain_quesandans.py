from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

loader = PyPDFLoader("patient_report.pdf")
pages = loader.load_and_split()

db = Chroma.from_documents(pages, OpenAIEmbeddings())
retriever = db.as_retriever()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_template(
    "Answer the question using the context below:\n\n{context}\n\nQuestion: {question}"
)

chain = (
    {
        "context": retriever,
        "question": lambda x: x
    }
    | prompt
    | llm
)

response = chain.invoke("What are the symptoms in this report?")
print(response.content)

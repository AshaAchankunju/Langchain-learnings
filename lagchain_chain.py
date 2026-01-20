from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(temperature=0.7)

symptom_prompt = ChatPromptTemplate.from_template(
    "Extract symptoms from this text: {text}"
)

diagnosis_prompt = ChatPromptTemplate.from_template(
    "Based on these symptoms: {symptoms}, suggest a possible medical condition."
)

chain = (
    symptom_prompt
    | llm
    | (lambda x: {"symptoms": x.content})
    | diagnosis_prompt
    | llm
)

result = chain.invoke(
    {"text": "I have headache, fever and shivering."}
)

print(result.content)

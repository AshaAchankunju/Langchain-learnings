from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
_ = load_dotenv(find_dotenv())

# Initialize OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# 1. calling the model
chat = ChatOpenAI(temperature=0.0)

# 2. create template
template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
prompt_template = ChatPromptTemplate.from_template(template_string)

# 3. create chain
chain = prompt_template | chat | StrOutputParser()

# 4. giving inputs
customer_style = "Arrogant Malayalam"
customer_email = "The service was very slow and I am not happy."

response = chain.invoke({"style": customer_style, "text": customer_email})
print(response)
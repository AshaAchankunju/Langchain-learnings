import os
import datetime
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# Load environment variables
_ = load_dotenv(find_dotenv())

# Initialize OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Model selection logic (you can simplify this now)
current_date = datetime.date.today()
target_date = datetime.date(2024, 6, 12)

if current_date > target_date:
    llm_model = "gpt-4.1-mini"  # recommended replacement
else:
    llm_model = "gpt-4.1-mini"

def get_completion(prompt, model=llm_model):
    response = client.responses.create(
        model=model,
        input=prompt,
        temperature=0,
    )
    return response.output_text

print(get_completion("What is 1 + 1?"))

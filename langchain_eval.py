from langsmith.evaluation import evaluate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

# 1. Define a prediction function
def predict(example):
    # Simulating your RAG / QA output
    return {
        "output": "The patient age is 45."
    }

# 2. Ground truth dataset
examples = [
    {
        "inputs": {
            "question": "what is the age of the patient in this medical report?"
        },
        "outputs": {
            "output": "The patient age is 45."
        }
    }
]

# 3. Run evaluation
results = evaluate(
    predict,
    data=examples,
    evaluators=["qa"]
)

print(results)
expected = "The patient age is 45."
predicted = "The patient age is 45."

grade = "CORRECT" if expected.lower() in predicted.lower() else "INCORRECT"

print("Question: what is the age of the patient?")
print("Expected:", expected)
print("Predicted:", predicted)
print("Grade:", grade)

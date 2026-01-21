from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

# 1. Set the model
llm = ChatOpenAI(temperature=0)

# 2. load the tools(example: Wikipedia, calculation 'llm-math')
# do"  pip install wikipedia numexpr "
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# 3. initialize agents
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True # it will help you see , how ai thinking
)

# 4. asking question
agent.run("Who is the current director of WHO? What is their current age raised to the power of 0.5?")
from langchain_openai import ChatOpenAI
from langchain_community.chains import ConversationChain
from langchain_community.memory import ConversationBufferMemory

# 1. set the model
llm = ChatOpenAI(temperature=0.0)

# 2. create a memory object
memory = ConversationBufferMemory()

# 3. create conversation chain
conversation = ConversationChain(
    llm=llm, 
    memory=memory,
    verbose=True # if give this true we can see how m/y goes in background
)

# 4.start conversation
conversation.predict(input="My name is asha.")
response = conversation.predict(input="do you remember my name?")

print(response) # o/p yes your name is asha."


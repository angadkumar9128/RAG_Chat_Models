from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)     
conversation = model.invoke("What is the speed of light?")
print(conversation.content)
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
load_dotenv()

llm = ChatMistralAI(model="mistral-medium-3-5")

while True:
    input_text = input("You: ")
    if input_text == "exit":
        break
    response = llm.invoke(input_text)
    print("Bot : " + response.content)
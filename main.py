from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

# Load environment variables
load_dotenv()

# Load PDF
loader = PyPDFLoader(
    r"C:\Users\kumar\Downloads\genai_roadmap_checklist.pdf"
)

docs = loader.load()

# Get content from page 3
page_content = docs[2].page_content

# Prompt Template
template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that summarizes document content in a concise manner."
        ),
        (
            "human",
            "Summarize the following content:\n\n{context}"
        )
    ]
)

# Create prompt
prompt = template.invoke(
    {
        "context": page_content
    }
)

# Initialize Mistral
llm = ChatMistralAI(
    model="mistral-medium-3-5"
)

# Generate response
response = llm.invoke(prompt)

print("\nSummary:")
print(response.content)
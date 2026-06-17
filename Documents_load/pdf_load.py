from langchain_community.document_loaders import PyPDFLoader 
loader = PyPDFLoader("C:/Users/kumar/Downloads/genai_roadmap_checklist.pdf")
data = loader.load() 
print(data[2])

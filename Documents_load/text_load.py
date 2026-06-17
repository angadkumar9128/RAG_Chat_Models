from langchain_community.document_loaders import TextLoader

data = TextLoader("C:/Users/kumar/OneDrive/Desktop/TextFiles/acc.txt").load()
print(data[1])
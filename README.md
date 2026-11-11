# RAG Chat Models

A Python learning and experimentation repository for using multiple large language model (LLM) providers through LangChain. It contains command-line examples, a Streamlit chat interface powered by Mistral, and starter scripts for loading PDF and text documents.

> **Status:** Early-stage experimentation. Despite the repository name, the current code does not implement a complete Retrieval-Augmented Generation (RAG) pipeline. Document loading is demonstrated, but chunking, embeddings, vector indexing, retrieval, and retrieval-grounded answer generation are not wired together.

## Project contents

| File | Purpose |
|---|---|
| main.py | Loads a PDF, selects its third page, and asks Mistral to summarize it with a LangChain prompt template. |
| mistral.py | Interactive terminal chat loop using Mistral. Enter exit to quit. |
| mistral_UI.py | Streamlit chat interface with session-based history and a clear-chat action. |
| Gemini_chat.py | Minimal Google Gemini invocation example. |
| groq_chat.py | Minimal Groq-hosted model invocation example. |
| openrouter_model.py | Minimal OpenRouter invocation example. |
| Documents_load/pdf_load.py | Loads a PDF using LangChain's PyPDFLoader. |
| Documents_load/text_load.py | Loads a text file using LangChain's TextLoader. |
| requirements.txt | Dependencies for the current examples and broader experiments. |

## Architecture

```text
Python examples
      |
   LangChain
      |
  +---+--------+-----------+
  |            |           |
Mistral      Gemini    Groq / OpenRouter
  |
Terminal chat or Streamlit UI

Document experiments
      |
PDFLoader / TextLoader
      |
Loaded pages / text
```

These are independent examples, not a unified model router or a completed RAG application.

## Technology stack

- Python
- LangChain and LangChain Community
- Mistral AI, Google Gemini, Groq, and OpenRouter integrations
- Streamlit
- PDF and text document loaders
- python-dotenv for environment configuration

## Getting started

### 1. Clone

```bash
git clone https://github.com/angadkumar9128/RAG_Chat_Models.git
cd RAG_Chat_Models
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The current requirements file does not include all provider adapters imported by the examples. Install the integrations you plan to use:

```bash
pip install langchain-mistralai langchain-google-genai langchain-groq langchain-openrouter
```

### 4. Configure API keys

Create a .env file in the project root. Add only the keys for providers you intend to use:

```dotenv
MISTRAL_API_KEY=your_mistral_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

Keep this file private. It is excluded by .gitignore. Never commit API keys.

### 5. Run an example

Mistral terminal chat:

```bash
python mistral.py
```

Mistral Streamlit interface:

```bash
streamlit run mistral_UI.py
```

Other provider examples:

```bash
python Gemini_chat.py
python groq_chat.py
python openrouter_model.py
```

PDF summarization:

```bash
python main.py
```

## Streamlit interface

Run streamlit run mistral_UI.py to launch the browser-based chat interface. The current UI includes chat-style messages, conversation history held in Streamlit session state, a clear-chat action, and a cached Mistral client.

**Known implementation detail:** the temperature slider is displayed but its selected value is not passed to the Mistral client. The model is currently initialized with a fixed temperature of 0.7.

## Document loading

The Documents_load folder contains introductory LangChain loader examples:

- PyPDFLoader loads PDF pages as document objects.
- TextLoader loads text files as document objects.

The scripts currently use hard-coded, machine-specific Windows paths. Update the paths in main.py, Documents_load/pdf_load.py, and Documents_load/text_load.py before running them. The PDF summarization example reads the third page, so its input PDF must contain at least three pages.

These examples perform document loading only. They do not yet split text into chunks, generate embeddings, populate a vector database, or retrieve context for an LLM.

## Current limitations and roadmap

Potential next steps for evolving this repository into a RAG application:

1. Replace hard-coded file paths with configuration or command-line arguments.
2. Split loaded documents into manageable chunks.
3. Generate embeddings for document chunks.
4. Persist and query a vector store such as Chroma.
5. Implement a retriever and a prompt that uses retrieved context.
6. Return source references and handle insufficient retrieval results.
7. Connect the Streamlit temperature control to model configuration.
8. Add provider selection, input validation, and clearer API error handling.
9. Add automated tests and document supported Python and package versions.

## Security

- Store credentials in environment variables or a local .env file.
- Do not commit secrets, private documents, or sensitive generated data.
- Review each hosted provider's data-handling policies before sending prompts or documents.

## Contributing

Contributions and improvements are welcome. For substantial changes, open an issue to discuss the proposed feature or implementation.

## License

There is currently no license file in this repository. Until a license is added, reuse, modification, and redistribution permissions are not explicitly granted.

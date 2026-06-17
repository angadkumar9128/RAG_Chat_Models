import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="AI Chat Model",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #4F46E5;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🤖 AI Chat Model</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Powered by LangChain + Mistral AI</div>',
    unsafe_allow_html=True
)

# Initialize LLM
@st.cache_resource
def load_llm():
    return ChatMistralAI(
        model="mistral-medium-3-5",
        temperature=0.7
    )

llm = load_llm()

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("""
    ### Features

    ✅ Mistral AI

    ✅ Chat History

    ✅ Beautiful UI

    ✅ Streamlit

    ✅ LangChain

    ✅ Fast Response
    """)

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Type your message..."):

    # User Message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(prompt)

            st.markdown(response.content)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )
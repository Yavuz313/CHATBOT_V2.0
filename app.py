import os
import time
import streamlit as st
from qa_loader import load_qa_and_create_vectorstore
from rag_chain import generate_response
from dotenv import load_dotenv

# 🔹 Load environment variables
load_dotenv()

# 🔹 Streamlit Page Configuration
st.set_page_config(page_title="Vistula University AI Assistant", layout="centered")

# 🔹 Title and Description
st.title("📚 Vistula University AI Assistant")
st.write("🚀 Ask me anything about Vistula University!")

# 🔹 Retrieve Data (Cached for Performance)
@st.cache_resource
def get_retriever():
    return load_qa_and_create_vectorstore()

retriever = get_retriever()

if isinstance(retriever, tuple):  
    retriever = retriever[0]

# 🔹 Start or Load Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🔹 Display Chat History
st.write("### 🗂️ Chat History")

for entry in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(entry["question"])
    with st.chat_message("assistant"):
        st.write(entry["answer"])

# 🔹 User Input
query = st.chat_input("Ask your question about Vistula University!")

# 🔹 Process When User Submits a Question
if query:
    with st.spinner("🤖 Thinking..."):
        response = generate_response(retriever, query)

    # 🔹 Add to Chat History
    st.session_state.chat_history.append({
        "question": query,
        "answer": response
    })

    # 🔹 Display User Question and AI Response
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("assistant"):
        placeholder = st.empty()
        current_text = ""

        # Typing Effect
        for word in response.split():
            current_text += word + " "
            placeholder.write(current_text)
            time.sleep(0.05)

# ui/streamlit_app.py

import streamlit as st
import tempfile
import os

def run_app(coordinator):
    st.set_page_config(page_title="Agentic RAG Chatbot", layout="wide")
    st.title("📚 Multi-Document QA Chatbot with MCP")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    uploaded_files = st.file_uploader("Upload documents (PDF, DOCX, CSV, PPTX, TXT)",
                                       type=["pdf", "docx", "csv", "pptx", "txt"],
                                       accept_multiple_files=True)

    if uploaded_files:
        file_paths = []
        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=file.name) as tmp:
                tmp.write(file.read())
                file_paths.append(tmp.name)
        coordinator.handle_file_upload(file_paths)
        st.success("Documents parsed and ingested.")

    query = st.text_input("Ask a question based on the uploaded documents")

    if query:
        st.session_state.chat_history.append(("You", query))
        coordinator.handle_question(query)
        answer = coordinator.get_last_answer()

        if answer:
            st.session_state.chat_history.append(("Bot", answer["answer"]))
            st.markdown("### 🧠 Answer")
            st.write(answer["answer"])

            st.markdown("### 📎 Source Chunks")
            for chunk in answer["sources"]:
                st.markdown(f"> {chunk}")

    if st.session_state.chat_history:
        st.sidebar.markdown("## 💬 Chat History")
        for speaker, text in reversed(st.session_state.chat_history):
            st.sidebar.markdown(f"**{speaker}:** {text}")
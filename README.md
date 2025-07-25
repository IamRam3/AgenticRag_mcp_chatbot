# 🧠 Agentic RAG Chatbot with Model Context Protocol (MCP)

This project implements an agent-based Retrieval-Augmented Generation (RAG) chatbot that can answer questions from uploaded documents of various formats (PDF, DOCX, PPTX, CSV, TXT). Agents communicate using a structured message format called Model Context Protocol (MCP).

---

## Demo & Explanation video
[Click to watch it.](https://drive.google.com/file/d/1Fsb5nhLsW7LGE6OW207jwTmBE5JD0ndw/view?usp=sharing)

---

## 🚀 Features

- ✅ Multi-format file parsing
- ✅ Vector search with FAISS
- ✅ OpenAI-based LLM answering
- ✅ Streamlit-based interactive UI
- ✅ Agentic architecture with MCP message passing

---

## 📁 Project Structure
```
.
├── agents/              # Ingestion, Retrieval, Response agents
├── core/                # MCP message protocol and file parsing utils
├── ui/                  # Streamlit-based UI
├── vectorstore/         # (Optional: FAISS wrapper if needed)
├── main.py              # Entry point
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🧪 Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/IamRam3/AgenticRag_mcp_chatbot.git
cd Agentic-rag-chatbot
```

2. **Install Dependencies**
```bash
uv add -r requirements.txt
```

3. **Set Groq API Key**

Place your Groq api key in **.env** file


4. **Run the App**
```bash
streamlit run main.py
```

---

## 🖼 Sample Use Case
- Upload a mix of PDFs, DOCX, CSVs, and PPTX slides
- Ask: "What KPIs were tracked in Q1?"
- The app will:
  1. Parse files (IngestionAgent)
  2. Retrieve top chunks (RetrievalAgent)
  3. Generate response (LLMResponseAgent)
  4. Show final answer and relevant sources

---

## 📌 Tech Stack
- **Inferencing**: Groq
- **LLM Model**: llama3-8b-8192
- **Embeddings**: Sentence Transformers (MiniLM)
- **Vector DB**: FAISS
- **UI**: Streamlit
- **Message Bus**: Custom MCP (in-memory)

---

## 📈 Future Improvements
- Multi-user session handling
- Persistent vector DB (ChromaDB, Weaviate)
- Chat history export
- Self-hosted LLM fallback

---

## 📮 Contact
For issues, please raise an issue or email: sairam68386@gmail.com

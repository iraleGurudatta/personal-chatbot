# Chatbot-RAG 🤖🔍

A real-time AI Search Assistant and Chatbot powered by **LangChain**, **LangGraph**, **Groq LLM**, and **Google Serper API**. This agent dynamically queries Google to answer real-time information requests.

---

## 📌 Features

- 🚀 **High-Speed Inference**: Powered by Groq LLM (`ChatGroq`) for rapid conversational responses.
- 🌐 **Real-time Web Search**: Integrated with `GoogleSerperAPIWrapper` to fetch live web search results.
- 🔄 **LangGraph Ready**: Configured via [`langgraph.json`](file:///c:/Users/LENOVO/Desktop/chatbot/langgraph.json) for execution and deployment with LangGraph CLI and LangGraph Studio.
- ⚡ **API Ready**: Supports REST API endpoints with **FastAPI** and **LangServe**.
- 🔒 **Secure Configuration**: Reads environment variables safely via `python-dotenv`.

---

## 🛠️ Tech Stack & Dependencies

- **Language**: Python 3.9+
- **Agent Framework**: [LangChain](https://www.langchain.com/) & [LangGraph](https://www.langchain-ai.github.io/langgraph/)
- **LLM Engine**: [Groq API](https://console.groq.com/) (`langchain-groq`)
- **Search Tool**: [Serper.dev Google Search API](https://serper.dev/) (`langchain-community`)
- **Web Server**: FastAPI / LangServe

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python installed and request API keys for:
- [Groq API Key](https://console.groq.com/)
- [Serper API Key](https://serper.dev/)

### 2. Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iraleGurudatta/personal-chatbot.git
   cd personal-chatbot
   ```

2. **Set up a virtual environment:**
   ```bash
   # Windows PowerShell / CMD
   python -m venv env
   .\env\Scripts\activate

   # macOS / Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Configuration

Create or edit the `.env` file in the root directory of the project:

```env
GROQ_API_KEY="your_groq_api_key_here"
SERPER_API_KEY="your_serper_api_key_here"
```

---

## 💻 Running the Application

### Option A: Using LangGraph CLI (Recommended)

Run the agent server using LangGraph CLI:

```bash
langgraph dev
```

### Option B: Running via Python Script

Execute [`chatbot.py`](file:///c:/Users/LENOVO/Desktop/chatbot/chatbot.py) directly:

```bash
python chatbot.py
```

### Option C: Serving via FastAPI & LangServe

Uncomment the FastAPI and LangServe routes in [`chatbot.py`](file:///c:/Users/LENOVO/Desktop/chatbot/chatbot.py):

```python
app = FastAPI(
    title="Chatbot API",
)

add_routes(
    app, 
    agent,
    path="/agent"
)
```

Then start the server using `uvicorn`:

```bash
uvicorn chatbot:app --reload
```

---

## 📂 Project Structure

```
chatbot/
├── chatbot.py        # Main agent definition & tool setup
├── langgraph.json    # LangGraph configuration
├── .env              # Environment variables file (API keys)
├── .gitignore        # Git ignore specifications
├── requirements.txt  # Python package dependencies
├── LICENSE           # License agreement
└── README.md         # Project documentation
```

---

## 📜 License

This project is licensed under the terms of the MIT / GNU GPL license in the [`LICENSE`](file:///c:/Users/LENOVO/Desktop/chatbot/LICENSE) file.
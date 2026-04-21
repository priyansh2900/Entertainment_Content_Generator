# Entertainment Content Generator

An AI-powered web application that generates professional screenplay scenes based on user input using **Generative AI, Retrieval-Augmented Generation (RAG), and Vector Search**.

The system allows users to enter a topic and select parameters such as **genre, mood, and scene length** to generate structured screenplay scenes automatically.

---

# Project Overview

Writing engaging screenplay scenes requires creativity and time. This project provides an **AI-assisted content generation tool** that helps generate screenplay scenes quickly using modern AI technologies.

The system integrates:

- **React Frontend** for user interaction  
- **FastAPI Backend** for API processing  
- **FAISS Vector Database** for similarity search  
- **Groq LLM API** for high-speed AI text generation  
- **Prompt Engineering** for structured screenplay generation  

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant screenplay knowledge before generating scenes.

---

# Key Features

- AI-powered screenplay scene generation  
- Retrieval-Augmented Generation (RAG) architecture  
- Vector similarity search using FAISS  
- Prompt engineering for structured script output  
- Interactive web interface for user input  
- Fast AI inference using Groq LLM API  
- Customizable parameters (genre, mood, scene length)

---

# System Architecture

The system follows a **layered architecture** consisting of multiple components:

```
User
 ↓
React Frontend
 ↓
FastAPI Backend
 ↓
Prompt Engineering Layer
 ↓
FAISS Vector Database (Context Retrieval)
 ↓
Groq LLM API (Scene Generation)
 ↓
Generated Screenplay Scene
```

---

# Workflow

1. User enters the topic in the web interface.
2. User selects genre, mood, and scene length.
3. React frontend sends API request to FastAPI backend.
4. Backend generates embeddings for the input query.
5. FAISS vector database retrieves relevant screenplay knowledge.
6. Prompt engineering module constructs a structured prompt.
7. The prompt is sent to the Groq LLM API.
8. The LLM generates the screenplay scene.
9. The generated output is displayed to the user.

---

# Technologies Used

```bash
| Technology | Purpose |
|---|---|
| React | Frontend interface |
| FastAPI | Backend API framework |
| Python | Backend programming |
| FAISS | Vector similarity search |
| Groq API | Large Language Model inference |
| Sentence Transformers | Embedding generation |
| HTML/CSS | UI design |
```
---

# Installation

### Clone the repository

```bash
git clone https://github.com/your-username/entertainment-content-generator.git
cd entertainment-content-generator
```

---

### Install backend dependencies

```bash
pip install -r requirements.txt
```

---

### Run FastAPI backend

```bash
uvicorn app:app --reload
```

---

### Run frontend

```bash
cd frontend
npm install
npm start
```

---

# API Endpoint

### Generate Screenplay Scene

**Endpoint**

```
POST /generate
```

**Request Body**

```json
{
  "topic": "Bank robbery scene",
  "genre": "Thriller",
  "mood": "Suspenseful",
  "scene_length": "Short"
}
```

**Response**

```json
{
  "scene": "Generated screenplay scene...",
  "retrieved_context": "Relevant screenplay guidelines..."
}
```

---

# Example Output

The system generates structured screenplay scenes including:

- Scene headings
- Character names
- Dialogues
- Action descriptions

Example:

```
EXT. DARK ALLEY – NIGHT

Rain falls heavily. Streetlights flicker.

JAKE
Leave her alone.

Two goons advance toward him...
```

---

# Project Structure

```
Entertainment-Content-Generator
│
├── backend
│   ├── app.py
│   ├── retriever.py
│   ├── prompt_engine.py
│
├── vector_database
│   ├── faiss_index.bin
│   ├── docs.pkl
│
├── frontend
│   ├── App.jsx
│   ├── Form.jsx
│   ├── Header.jsx
│   ├── OutputBox.jsx
│
├── requirements.txt
└── README.md
```

---

# Future Improvements

- Multi-scene story generation  
- Character generation module  
- Script summarization  
- Genre-based script templates  
- Export screenplay as PDF  
- Integration with voice or video generation  

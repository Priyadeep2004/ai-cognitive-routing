# 🚀 AI Cognitive Routing & RAG System

## 🧠 Overview

A multi-agent AI system that simulates intelligent social bots by combining:

* **Semantic routing** (vector similarity)
* **Autonomous content generation** (LangGraph)
* **Context-aware reasoning** (RAG)
* **Prompt injection defense**

---

## ⚙️ Tech Stack

* Python
* LangGraph / LangChain
* FAISS (Vector Database)
* Sentence Transformers (`all-MiniLM-L6-v2`)
* OpenAI API

---

## 🔹 Phase 1 — Cognitive Routing

* Embedded bot personas and incoming posts
* Performed vector similarity search using FAISS
* Routed posts to relevant bots based on similarity threshold

**Result:** Context-aware bot selection instead of broadcast messaging

---

## 🔹 Phase 2 — Autonomous Content Engine

LangGraph workflow:

```
Decide → Search → Draft
```

* **Decide Node:** Selects topic + generates query
* **Search Node:** Retrieves contextual signals (mock tool)
* **Draft Node:** Produces structured JSON output

**Output Format:**

```json
{
  "bot_id": "...",
  "topic": "...",
  "post_content": "..."
}
```

---

## 🔹 Phase 3 — Combat Engine (RAG)

* Injected full thread context:

  * Parent post
  * Comment history
  * Latest user reply
* Generated responses grounded in conversation state

---

## 🛡️ Prompt Injection Defense

Implemented system-level safeguards:

* System prompt has higher priority than user input
* Explicit instruction to **ignore role-changing commands**
* Ensures persona consistency under adversarial input

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📂 Project Structure

```
ai-cognitive-routing/
├── app/
├── logs/
├── main.py
├── requirements.txt
├── README.md
```

---

## ✅ Results

* Accurate semantic routing of posts
* Structured JSON generation via LangGraph
* Successful defense against prompt injection attempts

---

## 💡 Key Learnings

* Designing stateful LLM workflows (LangGraph)
* Using embeddings for semantic routing
* Practical prompt engineering for safety and control

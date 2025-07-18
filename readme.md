# 🧠 PostPilot — Modular GenAI Content Generator for Multiple Platforms

**PostPilot** is a modular, scalable AI content generation system that takes a single topic and produces high-quality, platform-optimized content (Twitter, LinkedIn, Blog, Facebook).  
It’s built with **LangChain + Gemini**, uses **parallel chains for performance**, and is designed from the ground up to be **easily reusable as a backend API**.

---

## 🚀 Highlights

✅ Modular chain-based architecture  
✅ Platform-specific generation using parallel chains  
✅ LLM-based review + improvement workflows  
✅ Clean, reusable logic — easily wrap into APIs  
✅ Streamlit UI for demonstration (separated from core logic)  
✅ Production-ready code structure

---

## 🧠 Why This Project Matters

PostPilot is not just a demo. It’s a **blueprint** for building LLM-powered systems the right way:
- All prompt logic is modularized
- Chain logic is isolated in callable functions
- Nothing is tightly coupled to the UI
- Can be reused instantly in **FastAPI**, **Flask**, **CLI**, **batch jobs**, or **scheduling systems**

---

## 🛠️ Tech Stack

| Component       | Technology               |
|------------------|---------------------------|
| LLM              | Gemini / OpenAI GPT       |
| Orchestration    | LangChain                 |
| UI (optional)    | Streamlit                 |
| Output Parsing   | Pydantic + custom formatters |
| Parallelism      | LangChain ParallelChain   |

---

## ⚙️ Architecture Overview

```text
[ Topic Input ]
      ⬇️
[ Parallel Post Generation Chain ]
      ⬇️
[ Review Chain ➡️ Improvement Chain ]
      ⬇️
[ Final Platform-Specific Outputs ]

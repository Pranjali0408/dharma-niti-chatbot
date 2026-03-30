# DharmaNiti – Indian Wisdom Chatbot

DharmaNiti is a lightweight web-based chatbot that provides simple, safe guidance inspired by **Bhagavad Gita** and **Chanakya Niti**.  
It uses a Flask backend and HTML/CSS/JavaScript frontend.

## Features

- **Indian wisdom answers**  
  - For each user question, the bot returns a relevant Bhagavad Gita verse + explanation  
  - And a Chanakya Niti quote with a practical takeaway

- **Theme detection**  
  - `work` – job, career, study, exams, etc.  
  - `mind` – stress, tension, sadness, low motivation, etc.  
  - `relations` – friends, family, love, trust, betrayal, etc.

- **Tags-based relevance**  
  - Each verse/quote has a list of `tags`  
  - The bot scores items by how many tags match the user’s question and picks the best match

- **Safe-mode (basic safety layer)**  
  - Detects highly sensitive queries (suicide / self-harm / severe harm)  
  - Always returns a hopeful Gita verse (e.g., 6.5)  
  - Plus a clear message that this bot is **not** a medical/mental health substitute and encourages talking to a trusted person or professional

- **Simple, modern UI**  
  - Flask + Jinja template  
  - Custom CSS with a dark theme, small “ॐ” logo, and chat bubbles

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Data:** JSON files (`data/gita_verses.json`, `data/chanakya_summaries.json`)

## Project Structure

```text
ai-chatbot-project/
│ app.py
│
├── data/
│   ├── gita_verses.json
│   └── chanakya_summaries.json
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/dharma-niti-chatbot.git
cd dharma-niti-chatbot
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv env
# Windows:
env\Scripts\activate
# Linux/macOS:
# source env/bin/activate
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the app

```bash
python app.py
```

Open in your browser:

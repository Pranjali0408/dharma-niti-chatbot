# DharmaNiti – Indian Wisdom Chatbot

DharmaNiti is a lightweight web-based chatbot that provides simple, safe guidance inspired by **Bhagavad Gita** and **Chanakya Niti**.  
It uses a Flask backend and HTML/CSS/JavaScript frontend.[page:0]

## Features

- **Indian wisdom answers**  
  - For each user question, the bot returns a relevant Bhagavad Gita verse + explanation.  
  - And a Chanakya Niti quote with a practical takeaway.[page:0]

- **Theme detection**  
  - `work` – job, career, study, exams, etc.  
  - `mind` – stress, tension, sadness, low motivation, etc.  
  - `relations` – friends, family, love, trust, betrayal, etc.[page:0]

- **Tags-based relevance**  
  - Each verse/quote has a list of `tags`.  
  - The bot scores items by how many tags match the user’s question and picks the best match.[page:0]

- **Safe-mode (basic safety layer)**  
  - Detects highly sensitive queries (suicide / self-harm / severe harm).  
  - Always returns a hopeful Gita verse (e.g., 6.5).  
  - Plus a clear message that this bot is **not** a medical/mental health substitute and encourages talking to a trusted person or professional.[page:0]

- **Simple, modern UI**  
  - Flask + Jinja template.  
  - Custom CSS with a dark theme, small “ॐ” logo, and chat bubbles.[page:0]

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Data:** JSON files (`data/gita_verses.json`, `data/chanakya_summaries.json`)[page:0]

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

Then open in your browser:

```text
http://127.0.0.1:5000/
```

You should now see the DharmaNiti chatbot UI running locally.[page:0]

---

## Note on GitHub Pages / Rendering

This project is built as a **Flask web app**, so the chatbot UI is rendered by the Python backend (`app.py`) and served at `http://localhost:5000` when you run it locally.[page:0]

When you open the GitHub Pages link:

> https://pranjali0408.github.io/dharma-niti-chatbot/

you will only see a static page generated from the repository (README-like view), **not** the live chatbot UI.[page:0][web:49]

This is expected because:

- GitHub Pages can host only **static files** (HTML, CSS, JS).  
- It cannot run a Python/Flask backend, so `app.py` never starts on GitHub Pages.[web:49]

### How to use this project right now

For now, I am using this project in two ways:

1. **Local demo (fully working chatbot)**  
   - Run `python app.py`.  
   - Open `http://localhost:5000` in the browser.  
   - This is what I use for demos, recordings, and testing.[page:0]

2. **Public code + documentation on GitHub Pages**  
   - The GitHub Pages URL is used only to show the repository content and documentation.  
   - It does not host the live Flask app itself.[page:0]

### Future deployment options (planned)

To make the chatbot accessible online without running it locally, I am exploring:

- **Option A – Deploy Flask backend on a Python-friendly hosting service**  
  - Host `app.py` on a platform that supports Python (e.g. Render / Railway / Fly.io).  
  - Serve both backend and frontend from there.[web:48]

- **Option B – Separate frontend on GitHub Pages + external API**  
  - Keep a static `index.html` + `script.js` on GitHub Pages.  
  - Update `script.js` to call the deployed Flask backend via an API endpoint such as `https://<backend-url>/chat` instead of `http://localhost:5000`.[web:48][web:49]

Until one of these deployment options is set up, **the chatbot will work only when run locally via `python app.py`** and will not appear as an interactive bot on the `github.io` URL.[page:0][web:49]

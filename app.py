from flask import Flask, render_template, request, jsonify
import random
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_data():
    gita_path = os.path.join(DATA_DIR, "gita_verses.json")
    chanakya_path = os.path.join(DATA_DIR, "chanakya_summaries.json")

    with open(gita_path, "r", encoding="utf-8") as f:
        gita_raw = json.load(f)
    with open(chanakya_path, "r", encoding="utf-8") as f:
        chanakya_raw = json.load(f)

    gita_by_theme = {}
    for item in gita_raw:
        theme = item.get("theme", "work")
        gita_by_theme.setdefault(theme, []).append(item)

    chanakya_by_theme = {}
    for item in chanakya_raw:
        theme = item.get("theme", "work")
        chanakya_by_theme.setdefault(theme, []).append(item)

    return gita_by_theme, chanakya_by_theme

GITA_QUOTES, CHANAKYA_QUOTES = load_data()

# Risky keywords (basic safe-mode)
RISK_KEYWORDS = [
    "suicide", "end my life", "kill myself", "self harm",
    "self-harm", "hurt myself", "maraaycha", "maraycha",
    "bomb", "terror", "murder"
]

def is_risky_question(question: str) -> bool:
    q = question.lower()
    return any(k in q for k in RISK_KEYWORDS)

def detect_theme(question: str) -> str:
    q = question.lower()

    if any(w in q for w in ["job", "work", "career", "study", "exam", "padhai", "kaam"]):
        return "work"

    if any(w in q for w in ["tension", "stress", "depress", "anxiety", "fear", "bhiti", "gussa", "anger", "sad"]):
        return "mind"

    if any(w in q for w in ["friend", "mitra", "love", "family", "relation", "husband", "wife", "bf", "gf", "betray"]):
        return "relations"

    return "work"

def select_best_by_tags(question: str, items: list) -> dict:
    q_words = question.lower().split()
    best_item = None
    best_score = -1

    for item in items:
        tags = [t.lower() for t in item.get("tags", [])]
        score = 0
        for w in q_words:
            if w in tags:
                score += 1
        if score > best_score:
            best_score = score
            best_item = item

    if best_item is None and items:
        best_item = random.choice(items)
    return best_item

def get_gita_by_ref(ref: str) -> dict:
    for theme, items in GITA_QUOTES.items():
        for it in items:
            if it.get("ref") == ref:
                return it
    return {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    # 1) Safe-mode for risky questions
    if is_risky_question(user_msg):
        # नेहमी 6.5 verse use कर
        gita = get_gita_by_ref("Bhagavad Gita 6.5")
        mind_list_chanakya = CHANAKYA_QUOTES.get("mind", [])
        chanakya = mind_list_chanakya[0] if mind_list_chanakya else {}

        safe_text = (
            "हा खूप संवेदनशील आणि महत्वाचा प्रश्न आहे.\n\n"
            "Gita असे सांगते की:\n"
            f"{gita.get('shlok', '')}\n"
            f"अर्थ: {gita.get('meaning', '')}\n\n"
            "Chanakya Niti थेट असे प्रश्न address करत नाही, पण आत्मसंयम आणि धैर्यावर भर देते.\n\n"
            "कृपया लक्षात ठेव:\n"
            "- तू एकटा/एकटी नाहीस.\n"
            "- अशा वेळी विश्वासू व्यक्ती, कुटुंबीय किंवा professional counselor शी बोलणे हेच सर्वात सुरक्षित आणि योग्य पाउल आहे.\n"
            "- हा bot फक्त सामान्य मार्गदर्शन देऊ शकतो, medical किंवा मानसिक आरोग्य उपचाराचा पर्याय नाही."
        )

        return jsonify({
            "theme": "safe_mode",
            "gita_ref": gita.get("ref", ""),
            "gita_shlok": gita.get("shlok", ""),
            "gita_meaning": gita.get("meaning", ""),
            "chanakya_ref": chanakya.get("ref", ""),
            "chanakya_text": chanakya.get("text", ""),
            "chanakya_practical": chanakya.get("practical", ""),
            "combined": safe_text
        })

    # 2) Normal flow
    theme = detect_theme(user_msg)

    gita_list = GITA_QUOTES.get(theme, GITA_QUOTES["work"])
    chanakya_list = CHANAKYA_QUOTES.get(theme, CHANAKYA_QUOTES["work"])

    gita = select_best_by_tags(user_msg, gita_list)
    chanakya = select_best_by_tags(user_msg, chanakya_list)

    combined = (
        f"Vishay: {theme}\n\n"
        "Gita असे सांगते की:\n"
        f"{gita['shlok']}\n"
        f"अर्थ: {gita['meaning']}\n\n"
        "Chanakya Niti असे सांगते की:\n"
        f"{chanakya['text']}\n"
        f"Practical अर्थ: {chanakya['practical']}"
    )

    return jsonify({
        "theme": theme,
        "gita_ref": gita["ref"],
        "gita_shlok": gita["shlok"],
        "gita_meaning": gita["meaning"],
        "chanakya_ref": chanakya["ref"],
        "chanakya_text": chanakya["text"],
        "chanakya_practical": chanakya["practical"],
        "combined": combined
    })

if __name__ == "__main__":
    app.run(debug=True)
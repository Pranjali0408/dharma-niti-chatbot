console.log("script.js loaded");
const chatWindow = document.getElementById("chat-window");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function addMessage(text, sender) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", sender);
    msgDiv.textContent = text;
    chatWindow.appendChild(msgDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    addMessage(text, "user");
    userInput.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: text })
        });

        const data = await response.json();

        const botText =
            `${data.gita_ref}\n` +
            `${data.gita_shlok}\n` +
            `अर्थ: ${data.gita_meaning}\n\n` +
            `${data.chanakya_ref}\n` +
            `${data.chanakya_text}\n` +
            `Practical: ${data.chanakya_practical}`;

        addMessage(botText, "bot");
    } catch (err) {
        addMessage("Error: server sathi request fail zali.", "bot");
        console.error(err);
    }
}

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        sendMessage();
    }
});
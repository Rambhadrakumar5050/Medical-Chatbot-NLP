function sendMessage() {
    let msg = document.getElementById("msg").value;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user">You: ${msg}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot">Bot: ${data.reply}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    document.getElementById("msg").value = "";
}
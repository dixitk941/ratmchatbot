function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBody = document.getElementById('chat-body');
    const userText = input.value.trim();
    if (!userText) return;

    // Show user message
    const userMsgDiv = document.createElement('div');
    userMsgDiv.className = 'user-message';
    userMsgDiv.textContent = userText;
    chatBody.appendChild(userMsgDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
    input.value = '';

    // Send to backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userText })
    })
    .then(res => res.json())
    .then(data => {
        const botMsgDiv = document.createElement('div');
        botMsgDiv.className = 'bot-message';
        botMsgDiv.textContent = data.response;
        chatBody.appendChild(botMsgDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    });
}

document.getElementById('user-input').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function presetSend(text) {
    document.getElementById('user-input').value = text;
    sendMessage();
}

document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');
    const chatInput = document.getElementById('chat-input');

    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const userMessage = chatInput.value;
        chatInput.value = '';

        const userMessageElement = document.createElement('div');
        userMessageElement.textContent = 'You: ' + userMessage;
        chatBox.appendChild(userMessageElement);

        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            const botMessageElement = document.createElement('div');
            botMessageElement.textContent = 'Bot: ' + data.response;
            chatBox.appendChild(botMessageElement);
        })
        .catch(error => console.error('Error:', error));
    });
});

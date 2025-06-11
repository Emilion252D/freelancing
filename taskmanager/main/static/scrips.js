document.addEventListener('DOMContentLoaded', function () {
    const messagesContainer = document.getElementById('messages');
    const chatId = messagesContainer.getAttribute('data-chat-id');
    const form = document.querySelector('.chat-form');
    const textarea = form.querySelector('textarea');

    async function fetchMessages() {
        try {
            const response = await fetch(/en/chats/api/messages/${chatId}/);
            const data = await response.json();
            messagesContainer.innerHTML = '';

            data.messages.forEach(msg => {
                const div = document.createElement('div');
                div.className = 'message ' + (msg.is_mine ? 'my-message' : 'other-message');
                div.innerHTML = `
                    <div class="message-info">
                        <strong>${msg.sender}</strong>
                        <span class="message-time">${msg.created_at}</span>
                    </div>
                    <div class="message-content">${msg.content}</div>
                `;
                messagesContainer.appendChild(div);
            });

            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        } catch (error) {
            console.error('Error fetching messages:', error);
        }
    }

    async function sendMessage(event) {
        event.preventDefault();

        const content = textarea.value.trim();
        if (!content) {
            return;
        }

        try {
            await fetch(/en/chats/api/send_message/${chatId}/, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({ content: content }),
            });

            textarea.value = '';
            fetchMessages();
        } catch (error) {
            console.error('Error sending message:', error);
        }
    }

    function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }

    form.addEventListener('submit', sendMessage);

    fetchMessages();
    setInterval(fetchMessages, 3000);
});
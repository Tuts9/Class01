// JavaScript
const chatbotButton = document.getElementById('chatbot-button');
const chatbotWindow = document.getElementById('chatbot-window');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatLog = document.getElementById('chat-log');

chatbotButton.addEventListener('click', () => {
  chatbotWindow.classList.remove('hidden');
});

sendButton.addEventListener('click', () => {
  const userInputValue = userInput.value;
  // Enviar mensagem para o servidor e receber resposta
  // ...
  chatLog.innerHTML += `<p class="mb-2">Você: ${userInputValue}</p>`;
  userInput.value = '';
});

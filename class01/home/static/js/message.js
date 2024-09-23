// Função que esconde o container de mensagens após 5 segundos (5000 milissegundos)
setTimeout(function() {
    let messageContainer = document.getElementById('message-container');
    if (messageContainer) {
        messageContainer.style.transition = "opacity 0.5s ease";
        messageContainer.style.opacity = "0"; // Inicia a transição
        setTimeout(function() {
            messageContainer.style.display = "none"; // Remove o elemento do DOM após a transição
        }, 500); // Aguarda o tempo da transição
    }
}, 2500); // Tempo para desaparecer (5 segundos)
const increaseButton = document.getElementById('increase-text');
const decreaseButton = document.getElementById('decrease-text');

let fontSize = localStorage.getItem('fontSize') ? parseInt(localStorage.getItem('fontSize')) : 100; // 100% é o tamanho padrão
const minFontSize = 100;  
const maxFontSize = 200;  // Define o limite em %

function applyFontSize() {
    document.documentElement.style.fontSize = fontSize + '%'; // Ajusta a fonte no html
}
applyFontSize();

increaseButton.addEventListener('click', () => {
    if (fontSize < maxFontSize) {
        fontSize += 10;
        localStorage.setItem('fontSize', fontSize);
        applyFontSize();
    }
});

decreaseButton.addEventListener('click', () => {
    if (fontSize > minFontSize) {
        fontSize -= 10;
        localStorage.setItem('fontSize', fontSize);
        applyFontSize();
    }
});
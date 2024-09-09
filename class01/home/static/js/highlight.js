// Variável que busca e armazena todos os botões
const headerButtons = document.querySelectorAll('nav > div > div > ul > li > a');

// Variável que busca e armazena todos os sections
const sections = document.querySelectorAll('main > section');

// Função que atualiza a classe dos botões para alteração das cores
function updateButtonColors() {
    // Loop que observa cada section conforme o scroll da página desce ou sobe
    sections.forEach(section => {
        // Variável que armazena o tamanho do elemento e a posição relativa ao viewport (área visivel para o usuario em tal momento)
        const sectionTop = section.getBoundingClientRect().top;

        // Verifica se a posição da section está favorável e cobre no mínimo 50% do viewport
        if (sectionTop >= 0 && sectionTop < window.innerHeight / 2) {
            // Variável que concatena aos elementos e armazena o valor igual ao link de referência dos botões
            const sectionId = '/#' + section.id;

            // Loop que verifica qual botão está com o link de referência igual ao id do section atual
            headerButtons.forEach(button => {
                if (button.getAttribute('href') === sectionId) {
                    button.classList.remove('text-white');
                    button.classList.add('text-blue-600');
                } else {
                    button.classList.remove('text-blue-600');
                    button.classList.add('text-white');
                }
            });
        }
    });
}
// Chamada de função para atualizar a cor do botão quando a página carrega pela primeira vez
updateButtonColors();
// Ação de evento que é ativada quando o scroll desce ou sobe
window.addEventListener('scroll', updateButtonColors);
// Seleciona o botão de troca de tema
const themeToggleBtn = document.getElementById('theme-toggle');
const htmlElement = document.documentElement; // O elemento <html>

// Verifica se o usuário já tem uma preferência armazenada
const storedTheme = localStorage.getItem('theme');
if (storedTheme) {
  htmlElement.classList.toggle('dark', storedTheme === 'dark');
}

// Adiciona o evento de clique no botão
themeToggleBtn.addEventListener('click', function() {
  // Alterna entre adicionar ou remover a classe 'dark' no elemento <html>
  htmlElement.classList.toggle('dark');

  // Armazena a preferência do usuário no localStorage
  if (htmlElement.classList.contains('dark')) {
    localStorage.setItem('theme', 'dark');
  } else {
    localStorage.setItem('theme', 'light');
  }
});

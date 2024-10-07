// Check the user's saved theme preference on page load
document.addEventListener('DOMContentLoaded', function () {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.documentElement.classList.add('dark');
    } else if (theme === 'light') {
        document.documentElement.classList.remove('dark');
    }
});

// Function to toggle the theme and save the preference
function toggleTheme() {
    if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    }
}

// Attach the toggle function to the button with the ID 'theme-toggle-button'
document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('theme-toggle-button');
    if (toggleButton) {
        toggleButton.addEventListener('click', toggleTheme);
    }
});


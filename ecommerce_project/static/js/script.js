// Global JavaScript for interactions
console.log("ABStore loaded successfully.");

document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const menuBtn = document.getElementById('mobile-menu-btn');
    const navbarMenu = document.getElementById('navbar-menu');

    if (menuBtn && navbarMenu) {
        menuBtn.addEventListener('click', () => {
            navbarMenu.classList.toggle('active');
        });
    }
});

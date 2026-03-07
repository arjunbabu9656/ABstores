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

    // Scroll Animations using Intersection Observer
    const animatedElements = document.querySelectorAll('.card, .hero-section, .alert, .slide-in-left, .slide-in-right, .store-sidebar');

    // Add the animation class to elements
    animatedElements.forEach((el, index) => {
        if (!el.classList.contains('slide-in-left') && !el.classList.contains('slide-in-right')) {
            el.classList.add('animate-on-scroll');
        }

        // Add staggered delay to cards in a grid
        if (el.classList.contains('card')) {
            const delay = (index % 4) * 100; // 0, 100, 200, 300ms
            if (delay > 0) el.classList.add(`delay-${delay}`);
        }
    });

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // Trigger when 15% of the element is visible
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                // Optional: Stop observing once animated if we only want it to happen once
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    animatedElements.forEach(el => {
        scrollObserver.observe(el);
    });

    // Card Animations (Desktop Only)
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        // 1. Click Animation
        card.addEventListener('click', () => {
            if (window.innerWidth > 768) {
                card.classList.add('card-clicked');
            }
        });
    });
});

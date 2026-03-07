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

    // Custom Cursor Logic
    const cursorDot = document.createElement('div');
    cursorDot.classList.add('custom-cursor-dot');
    document.body.appendChild(cursorDot);

    const cursorOutline = document.createElement('div');
    cursorOutline.classList.add('custom-cursor-outline');
    document.body.appendChild(cursorOutline);

    window.addEventListener('mousemove', (e) => {
        const posX = e.clientX;
        const posY = e.clientY;

        cursorDot.style.left = `${posX}px`;
        cursorDot.style.top = `${posY}px`;

        // Slight delay on outline for smooth trailing effect
        cursorOutline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: "forwards" });
    });

    // Add hovering effect to links and buttons
    const interactables = document.querySelectorAll('a, button, .btn');
    interactables.forEach(el => {
        el.addEventListener('mouseenter', () => cursorOutline.classList.add('hovering'));
        el.addEventListener('mouseleave', () => cursorOutline.classList.remove('hovering'));
    });

    // 3D Tilt Effect for Cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = ((y - centerY) / centerY) * -10; // Max rotation 10deg
            const rotateY = ((x - centerX) / centerX) * 10;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.05, 1.05, 1.05)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
            card.style.transition = 'transform 0.5s ease';
        });

        card.addEventListener('mouseenter', () => {
            card.style.transition = 'none'; // Remove transition when entering for instant tracking
        });
    });
});

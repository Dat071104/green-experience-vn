document.addEventListener('DOMContentLoaded', () => {
    // 1. Lucide icons init
    lucide.createIcons();

    // 2. Scroll reveal IntersectionObserver
    const observer = new IntersectionObserver(
        (entries) => entries.forEach(e => e.isIntersecting && e.target.classList.add('visible')),
        { threshold: 0.15 }
    );
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // 3. Mobile nav toggle
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // 4. Flash message auto-dismiss (3s)
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = '0';
            setTimeout(() => msg.remove(), 300);
        }, 3000);

        const closeBtn = msg.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 300);
            });
        }
    });

    // 6. Active nav link highlight
    const currentPath = window.location.pathname;
    const navItems = document.querySelectorAll('.nav-links a');
    navItems.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath.startsWith(href) && href !== '/')) {
            link.classList.add('active');
        }
    });
});

// 5. Format VND helper
window.formatVND = function(amount) {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(amount).replace('₫', '₫').replace(/,/g, '.');
};

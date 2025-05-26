// DOM Ready
document.addEventListener("DOMContentLoaded", function () {
    // Smooth Scroll
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scroll({
                    top: target.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });
});


    
    // Animating Section Elements on Scroll
    const animatedSections = document.querySelectorAll('.section');
    window.addEventListener('scroll', function () {
        animatedSections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            if (sectionTop < windowHeight - 50) {
                section.classList.add('visible');
            }
        });
    });

    // Interactive Button Animation for Test Button
    const startTestButton = document.querySelector('.btn-success');
    startTestButton.addEventListener('mouseover', function () {
        startTestButton.classList.add('animate__pulse');
    });
    startTestButton.addEventListener('mouseout', function () {
        startTestButton.classList.remove('animate__pulse');
    });

    // Dropdown Menu Interaction
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    dropdownToggle.addEventListener('click', function (e) {
        e.preventDefault();
        dropdownMenu.classList.toggle('show');
    });

    // Close Dropdown when clicking outside
    document.addEventListener('click', function (e) {
        if (!dropdownToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
            dropdownMenu.classList.remove('show');
        }
    });



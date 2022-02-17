window.addEventListener('scroll', () => {
    if (window.scrollY >= 300) {
        document.querySelector('nav').classList.add('shadow-bg');
        document.querySelector('nav').classList.remove('transparent');
    } else {
        document.querySelector('nav').classList.remove('shadow-bg');
        document.querySelector('nav').classList.add('transparent');
    }
})
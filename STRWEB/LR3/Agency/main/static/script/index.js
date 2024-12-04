document.querySelectorAll('.property-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const x = (e.clientX - card.offsetLeft) / card.offsetWidth;
        const y = (e.clientY - card.offsetTop) / card.offsetHeight;
        card.style.transform = `translate(${(x - 0.5) * 20}px, ${(y - 0.5) * 20}px)`;
    });
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translate(0, 0)';
    });
})
console.log('Community JS loaded');
document.querySelectorAll('.post-card').forEach(card => {
    card.addEventListener('click', () => {
        window.location = card.dataset.url;
    });
});
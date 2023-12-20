document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.lazyload');
// 
const imagepath = 'photos/images/';
// 
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            }

            const image = entry.target;
            image.src = imagepath;
            observer.unobserve(image);
        });
    });

    images.forEach(image => {
        imageObserver.observe(image);
    });
});

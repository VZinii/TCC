// Controles do player de vídeo:

const botoesDePlay = document.querySelectorAll('.play-button');

botoesDePlay.forEach(botao => {

    botao.addEventListener('click', () => {

        video = botao.parentElement.previousElementSibling;

        video.play();
        botao.style.display = 'none';
    });

    video = botao.parentElement.previousElementSibling;

    video.addEventListener('pause', () => {
        
        botao.style.display = 'flex';
    });

    video.addEventListener('ended', () => {
        
        botao.style.display = 'flex';
    });

});
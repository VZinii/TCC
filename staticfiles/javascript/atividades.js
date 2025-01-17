const form = document.querySelector('.resposta-form');

const mensagemErro = document.querySelector('.mensagem-erro');

const barraVidas = document.querySelector('div.vidas');

form.addEventListener('submit', e => {
    e.preventDefault();
    
    avancar().then(data => {

        if ( data.acertou ){

            // Já atualizei o progresso das atividades da seção no backend, basta reiniciar o frontend
            location.reload();

        } else {

            mensagemErro.classList.remove('d-none');

            const spanResposta = mensagemErro.lastElementChild;

            let respostaCorreta = "";

            let input, label;

            switch ( data.resposta_correta ){
                case 'V':
                    input = form.verdadeiro;
                    respostaCorreta = "Verdadeiro";
                    travarResposta(input);
                    break;
                case 'F':
                    input = form.falso;
                    respostaCorreta = "Falso";
                    travarResposta(input);
                    break;
                case 'A':
                    input = form.opcaoA;
                    label = input.nextElementSibling;
                    respostaCorreta = label.textContent;
                    travarResposta(input);
                    break;
                case 'B':
                    input = form.opcaoB;
                    label = input.nextElementSibling;
                    respostaCorreta = label.textContent;
                    travarResposta(input);
                    break;
                case 'C':
                    input = form.opcaoC;
                    label = input.nextElementSibling;
                    respostaCorreta = label.textContent;
                    travarResposta(input);
                    break;
                default:
                    // As respostas corretas acima precisam de formatação, caso contrário, basta pegar a resposta recuperada do endpoint
                    respostaCorreta = data.resposta_correta;
            }
            
            spanResposta.textContent += ' ' + respostaCorreta;

            removerUmaVida().then(dados => {

                if ( dados.status === "sucesso" ){
                    atualizaVidas();
                }
                else {
                    console.log(dados.mensagem);
                }

            }).catch(erro => {

                console.log(erro);
            });

        }

    }).catch(erro => {

        console.log('rejected', erro);
    });
});

const avancar = async () => {

    const formData = new FormData();
    formData.append('resposta', form.resposta.value);

    const response = await fetch('./checar', {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        body: formData,
        mode: 'same-origin', // Do not send CSRF token to another domain.
    });
    
    return await response.json();
};

const travarResposta = resposta => {

    const todosInputs = document.querySelectorAll('input');

    todosInputs.forEach( (input) => {

        if ( input !== resposta ){
            input.setAttribute('disabled', '');
        }
        else {
            form.resposta.value = input.value;
        }

    });

};

const removerUmaVida = async () => {

    const response = await fetch('http://localhost:8000/removeVida');

    return await response.json();

};

const atualizaVidas = () => {

    fetch('http://localhost:8000/obterVidas').then(response => {

        return response.json();

    }).then(dados => {

        barraVidas.innerHTML = "";

        for (i=0; i < dados.vidas; i++ ){
            
            barraVidas.innerHTML += '<img src="https://cdn-icons-png.flaticon.com/512/833/833472.png" width="32" height="32" alt="Coração" class="m-1 img-small">';
        }

    }).catch(error => {

        console.log(error);
    });
};

atualizaVidas();

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
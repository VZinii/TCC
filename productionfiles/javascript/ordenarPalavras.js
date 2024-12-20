const caixaResposta = document.querySelector('.caixa-resposta');

const secaoPalavras = document.querySelector('#palavras');

const secaoResposta = document.querySelector('#resposta');

const inputResposta = document.querySelector('input.d-none'); // Referencia para o input escondido na página

caixaResposta.addEventListener('click', e => {
    e.preventDefault();

    if ( e.target.parentElement === secaoPalavras ){
        
        const palavra = e.target;
        // Removo da seção de palavras
        e.target.remove();
        // E adiciono na seção de resposta
        secaoResposta.appendChild(palavra);

        //Além disso, preencho o input com a resposta, para poder levar isso ao backend
        inputResposta.value += palavra.textContent + ' ';

    } else if ( e.target.parentElement === secaoResposta ){

        const palavra = e.target;
        // Removo da seção de resposta
        e.target.remove();

        // E adiciono na seção de palavras
        secaoPalavras.appendChild(palavra);

        // Remove a palavra da resposta:
        inputResposta.value = inputResposta.value.replace(palavra.textContent+' ', '');
    }

});
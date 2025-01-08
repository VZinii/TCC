const containerItens = document.querySelector('#itens-loja');
const ouroUsuario = Number(document.querySelector('#ouroUsuario').textContent);

containerItens.addEventListener('click', e => {

    
});

const botoesComprar = document.querySelectorAll('button.item');

botoesComprar.forEach(botao => {

    const valorItem = Number(botao.previousElementSibling.querySelector('p').textContent);

    if ( valorItem > ouroUsuario ){
        botao.classList.add('disabled');
    }
})
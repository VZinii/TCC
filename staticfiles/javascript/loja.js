const containerItens = document.querySelector('#itens-loja');
const ouroUsuario = Number(document.querySelector('#ouroUsuario').textContent);
const divOuroUsuario = document.querySelector('#ouroUsuario').parentElement;

containerItens.addEventListener('click', e => {

    if ( e.target.classList.contains('item', 'btn')  ){
        // Significa que clicou no botão de comprar algum item
        textoItem = e.target.previousElementSibling.textContent;

        if ( textoItem.includes('Vida Extra') ){ // Se é o item "Vida Extra"
            comprarVida().then(dados => {

                if (dados.status === "sucesso"){
                    atualizarOuroPagina();
                } else{

                    alert(dados.mensagem);
                }
                
            }).catch(erro => {
                console.log(erro);
            });
        }
    }

});

const atualizarOuroPagina = () => {

    fetch('http://localhost:8000/obterOuro').then(response => {

        return response.json();

    }).then(dados => {

        divOuroUsuario.innerHTML = '';

        divOuroUsuario.innerHTML += 
            `<h4 id="ouroUsuario" class="me-2">${dados.ouro}</h4>
            <img class="mb-2" src="https://cdn-icons-png.flaticon.com/512/1800/1800205.png" alt="" height="25" width="25">`

        atualizarBotoes(dados.ouro);

    }).catch(error => {

        console.log(error);
    });
};
 
const botoesComprar = document.querySelectorAll('button.item');

const atualizarBotoes = (ouro) => {

    botoesComprar.forEach(botao => {

        const valorItem = Number(botao.previousElementSibling.querySelector('p').textContent);

        if ( valorItem > ouro ){
            botao.classList.add('disabled');
        }
    });
};

const comprarVida = async () => {

    const response = await fetch('http://localhost:8000/comprarVida');

    return await response.json()
};

atualizarBotoes(Number(ouroUsuario));
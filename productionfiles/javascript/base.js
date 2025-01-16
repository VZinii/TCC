// Botão de abrir a sidebar que fica ao lado da sidebar
document.getElementById('botao-abrir-interno').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('col-xxl-3');
    document.getElementById('sidebar').classList.toggle('vh-100');
    document.getElementById('sidebar').classList.toggle('d-none');
    document.getElementById('conteudo').classList.toggle('col-xxl-9');
    document.getElementById('botao-abrir-externo').classList.toggle('d-none');
});

// Botão de abrir a sidebar que fica fixa no canto superior direito da página, quando a sidebar é omitida ou quando é um dispotivo móvel
document.getElementById('botao-abrir-externo').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('col-xxl-3');
    document.getElementById('sidebar').classList.toggle('vh-100');
    document.getElementById('sidebar').classList.toggle('d-none');
    document.getElementById('conteudo').classList.toggle('col-xxl-9');
    document.getElementById('botao-abrir-externo').classList.toggle('d-none');
});

const sideBarItens = document.querySelector('#sidebar-itens');

sideBarItens.addEventListener('click', e => {
    // Limpa todos e depois aplica no que foi clicado

    const todosOsItens = document.querySelectorAll('.nav-link');

    todosOsItens.forEach(item => {
        item.classList.remove('active');
    });

    if (e.target.tagName == 'A'){
        e.target.classList.add('active');
    }
    else if ( e.target.tagName == 'IMG' || e.target.tagName == 'SPAN') {
        e.target.parentElement.classList.add('active');
    }

});

const ativarSideLink = () => {

    const url = document.URL;

    const todosOsItens = document.querySelectorAll('.nav-link');

    todosOsItens.forEach(item => {
        item.classList.remove('active');

        if (url.includes('perfil') && item.textContent.includes("Perfil")){
            item.classList.add('active');
        } else if (url.includes('missoes') && item.textContent.includes("Missões")){
            item.classList.add('active');
        } else if (url.includes('loja') && item.textContent.includes("Loja")){
            item.classList.add('active');
        } else if (url.includes('amigos') && item.textContent.includes("Amigos")){
            item.classList.add('active');
        } else if (url.includes('configuracoes') && item.textContent.includes("Configurações")){
            item.classList.add('active');
        } else if ( (url === "http://localhost:8000/" || url.includes('modulo')) && item.textContent.includes("Aprender")){
            item.classList.add('active');
        }

    });

}

ativarSideLink();

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
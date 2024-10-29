document.getElementById('botao-abrir-interno').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('col-3');
    document.getElementById('sidebar').classList.toggle('vh-100');
    document.getElementById('sidebar').classList.toggle('w-0');
    document.getElementById('conteudo').classList.toggle('col-9');
    document.getElementById('botao-abrir-externo').classList.toggle('d-none');
});

document.getElementById('botao-abrir-externo').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('col-3');
    document.getElementById('sidebar').classList.toggle('vh-100');
    document.getElementById('sidebar').classList.toggle('w-0');
    document.getElementById('conteudo').classList.toggle('col-9');
    document.getElementById('botao-abrir-externo').classList.toggle('d-none');
});
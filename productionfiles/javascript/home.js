// const modulos = document.querySelector('.modulos');

// modulos.addEventListener('click', e => {
//     console.log(e);
// });

const botoes = document.querySelectorAll('.botao-entrar');

botoes.forEach( botao => {

    botao.addEventListener('click', function() {

        //const id_modulo = this.getAttribute('modulo-id');

        // fetch(`/modulo/${id_modulo}/`, {
        //     method: 'GET',
        // })
        // .then(response => {
        //     if (!response.ok) {
        //         throw new Error('Erro ao acessar módulo');
        //     }
        //     window.location.href = `/modulo/${id_modulo}`;
        // })
        // .catch(error => {
        //     console.error('Erro ao acessar módulo:', error.message);
        // });
        
    });
});
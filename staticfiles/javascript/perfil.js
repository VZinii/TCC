const ctx = document.getElementById('graficoNumVolumes');

let barColors = ["green", "blue","yellow"];

new Chart(ctx, {
    type: "bar",
    data: {
        labels: vrotulos,
        datasets: [{
            backgroundColor: barColors,
            data: vdados,
        }]
    },
    options: {
        plugins: {
            legend: {display: false},
            title: {
                display: true,
                text: "Progresso de Aprendizagem em %"
            },
        },
        scales: {
            y: {
                min: 0,
                max: 100,
            }
        }
    }
});
const ctx = document.getElementById('graficoNumVolumes');

let xValues = ["Introdução", "Intermediário", "Avançado"];
let yValues = [55, 49, 44, 24, 15];
let barColors = ["green", "blue","yellow"];

new Chart(ctx, {
    type: "bar",
    data: {
        labels: xValues,
        datasets: [{
            backgroundColor: barColors,
            data: yValues
        }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Progresso de Aprendizagem"
        }
    }
});
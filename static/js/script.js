// Función para crear un gráfico de tipo barra
function createBarChart(canvasId, labels, data, backgroundColor, borderColor, titleText) {
    const ctx = document.querySelector(canvasId).getContext('2d');
    const dataSet = {
        labels: labels,
        datasets: [{
            maxBarThickness: 30,
            minBarLength: 4,
            data: data,
            backgroundColor: backgroundColor,
            borderColor: borderColor
        }]
    };

    const config = {
        type: 'bar',
        data: dataSet,
        options: {
            title: {
                display: true,
                text: titleText,
                fontSize: 18,
            },
            legend: {
                display: false,
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                xAxes: [{
                    gridLines: {
                        offsetGridLines: true
                    }
                }]
            }
        }
    };

    new Chart(ctx, config);
}

// Función para crear un gráfico de tipo torta
function createPieChart(canvasId, labels, data, backgroundColor, borderColor, titleText) {
    const ctx = document.querySelector(canvasId).getContext('2d');
    const dataSet = {
        labels: labels,
        datasets: [{
            data: data,
            backgroundColor: backgroundColor,
            borderColor: borderColor
        }]
    };

    const config = {
        type: 'pie',
        data: dataSet,
        options: {
            title: {
                display: true,
                text: titleText,
                fontSize: 18,
            },
            legend: {
                display: true,
            }
        }
    };

    new Chart(ctx, config);
}

// Datos y configuración para cada gráfico
const graphConfigs = [
    {
        canvasId: "#grafica3",
        labels: aLooses.map(element => element[0]),
        data: aLooses.map(element => element[1]),
        backgroundColor: '#1414b8',
        borderColor: 'white',
        titleText: "Perdidas por mes $"
    },
    {
        canvasId: "#grafica4",
        labels: aAssets.map(element => element[0]),
        data: aAssets.map(element => element[1]),
        backgroundColor: '#293614',
        borderColor: 'white',
        titleText: "Activo por mes $"
    },
    {
        canvasId: "#grafica5",
        labels: Looses_by.map(element => element[0]),
        data: Looses_by.map(element => element[1]),
        backgroundColor: ['rgb(69,177,223)', 'rgb(99,201,122)', 'rgb(203,82,82)', 'rgb(229,224,88)', 'rgb(119,127,173)', 'rgb(139,151,72)', 'rgb(253,32,32)', 'rgb(279,174,38)'],
        borderColor: ['grey','grey','grey','grey','grey','grey','grey','grey'],
        titleText: "Tipo de Gasto acumulado en $"
    },
    {
        canvasId: "#grafica6",
        labels: liabilities.map(element => element[0]),
        data: liabilities.map(element => element[1]),
        backgroundColor: '#1414b8',
        borderColor: 'white',
        titleText: "Pasivo por mes $"
    }
];

// Crear gráficos
graphConfigs.forEach(config => {
    if (config.canvasId === "#grafica5") {
        createPieChart(config.canvasId, config.labels, config.data, config.backgroundColor, config.borderColor, config.titleText);
    } else {
        createBarChart(config.canvasId, config.labels, config.data, config.backgroundColor, config.borderColor, config.titleText);
    }
});
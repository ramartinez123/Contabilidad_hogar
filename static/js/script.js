const colors3 = ['#4e6b21','#293614','#4e6b21', '#719c30', '#67823a', '#99c255','#131a09',
'#293614', '#4e6b21','#719c30','#67823a','#99c255', '#131a09','#293614', '#4e6b2'];
const colorsb3 = ['white'];
const graph3 = document.querySelector("#grafica3");

const data_3=[] 
const label_3= [] 
aLooses.forEach(element => data_3.push(element[1]))
aLooses.forEach(element => label_3.push(element[0]))
console.log(data_3,label_3)
   
const data3 = {

        labels: label_3,
        datasets: [{
            //barThickness: 20,
            maxBarThickness: 30,
            minBarLength: 4,
            data: data_3,
            backgroundColor: '#1414b8',
            borderColor: colorsb3
        }]
    };
    const config3 = {
        type: 'bar',
        data: data3,
        options : {
            title: {
                display: true,
                text: "Perdidas por mes $ ",
                fontSize: 18    ,
           },
            legend: {
                display: false, 
            },
            
            scales: {
                yAxes: [{
                    ticks: {
                      beginAtZero: true
                    },

                }],

                xAxes: [{
  
                    gridLines: {
                        offsetGridLines: true
                    },  
                }]
            }
        }

    };

new Chart(graph3, config3);


const colors4 = ['#4e6b21','#293614','#4e6b21', '#719c30', '#67823a', '#99c255','#131a09',
'#293614', '#4e6b21','#719c30','#67823a','#99c255', '#131a09','#293614', '#4e6b2'];
const colorsb4 = ['white'];
const graph4 = document.querySelector("#grafica4");
const data_4=[] 
const label_4= [] 
aAssets.forEach(element => data_4.push(element[1]))
aAssets.forEach(element => label_4.push(element[0]))
console.log(data_4,label_4)
const data4 = {

        labels: label_4,
        datasets: [{
            //barThickness: 20,
            maxBarThickness: 30,
            minBarLength: 4,
            data: data_4,
            backgroundColor: '#293614',
            borderColor: colorsb4
        }]
    };
    const config4 = {
        type: 'bar',
        data: data4,
        options : {
            title: {
                display: true,
                text: "Activo por mes $ ",
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
                    },  
                }]

            }
        }
    };

new Chart(graph4, config4);

const colors5 = ['rgb(69,177,223)', 'rgb(99,201,122)', 'rgb(203,82,82)', 'rgb(229,224,88)','rgb(119,127,173)', 'rgb(139,151,72)', 'rgb(253,32,32)', 'rgb(279,174,38)'];
const colorsb5 = ['grey','grey','grey','grey','greyk','grey','grey','grey','grey'   ];
const graph5 = document.querySelector("#grafica5");
const data_5= [] 
const label_5= [] 
Looses_by.forEach(element => data_5.push(element[1]))
Looses_by.forEach(element => label_5.push(element[0]))
console.log(data_5,label_5)
const data5 = {

        labels: label_5,
        datasets: [{
            //barThickness: 20,
            maxBarThickness: 30,
            minBarLength: 4,    
            data: data_5,
            backgroundColor: colors5,
            borderColor: colorsb5
        }]
    };

    const config5 = {
        type: 'pie',    
        data: data5,
        options : {
            title: {
                display: true,
                text: "Tipo de Gasto acumulado en $ ",
                fontSize: 18,
           },
            legend: {
                display: true       ,
            },  
            
           
        }
    };

new Chart(graph5, config5);

const colors6 = ['#4e6b21','#293614','#4e6b21', '#719c30', '#67823a', '#99c255','#131a09',
'#293614', '#4e6b21','#719c30','#67823a','#99c255', '#131a09','#293614', '#4e6b2'];
const colorsb6 = ['white'];
const graph6 = document.querySelector("#grafica6");
const data_6=[] 
const label_6= [] 
liabilities.forEach(element => data_6.push(element[1]))
liabilities.forEach(element => label_6.push(element[0]))
console.log(data_6,label_6)
const data6 = {

        labels: label_6,
        datasets: [{
            //barThickness: 20,
            maxBarThickness: 30,
            minBarLength: 4,
            data: data_6,
            backgroundColor: '#1414b8',
            borderColor: colorsb6
        }]
    };
    const config6 = {
        type: 'bar',
        data: data6,
        options : {
            title: {
                display: true,
                text: "Pasivo por mes $ ",
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
                    },  
                }]

            }
        }
    };

new Chart(graph6, config6);

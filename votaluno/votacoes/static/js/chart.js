let primeiroGrafico = document.getElementById('primeiroGrafico').getContext('2d');

let chart = new Chart(primeiroGrafico, {
    type: 'line',
    data: {
        labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
        datasets: [{
                label: 'Eventos',
                data: [11200, 13000, 18260, 15500, 16965, 17000],
                backgroundColor: "#5e35b19d",
                borderColor: "#5e35b1"
            },
            {
                label: 'Pessoas',
                data: [20112, 16569, 16203, 17257, 20852, 20698],
                backgroundColor: "#ff6f269d",
                borderColor: "#ff6f26"
            }
        ]
    }, 
    options: {
        responsive: true,
        display: true,
    }
});


let segundo = document.getElementById('segundoGrafico').getContext('2d');

let chart2 = new Chart(segundo, {
    type: 'doughnut',
    data: {
        labels: ["Eventos", "Pessoas", "Lotação", "Chamados"],
        datasets: [
          {
            backgroundColor: ["#5e35b1", "#ff6f26","#ffa726","#789dc9"],
            data: [17000,20268,11004,50852]
          }
        ]
      },
      options: {
        title: {
          display: true,
          text: 'Operações no sistema'
        }
      }
  });
  
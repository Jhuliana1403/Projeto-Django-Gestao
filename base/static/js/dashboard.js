document.addEventListener("DOMContentLoaded", function () {
    // Gráfico Financeiro Comparativo
    var ctxFinanceiro = document.getElementById("graficoFinanceiro").getContext("2d");
    new Chart(ctxFinanceiro, {
        type: "bar",
        data: {
            labels: ["Salários", "Pagamentos"],
            datasets: [{
                label: "Valores em R$",
                data: [
                    parseFloat(document.getElementById("graficoFinanceiro").dataset.salarios),
                    parseFloat(document.getElementById("graficoFinanceiro").dataset.pagamentos)
                ],
                backgroundColor: ["#3498db", "#e74c3c"]
            }]
        },
        options: { responsive: true }
    });

    // Gráfico de Pagamentos Mensais
    var ctxMensal = document.getElementById("graficoMensal").getContext("2d");
    new Chart(ctxMensal, {
        type: "line",
        data: {
            labels: document.getElementById("graficoMensal").dataset.meses.split(","),
            datasets: [{
                label: "Pagamentos Mensais (R$)",
                data: document.getElementById("graficoMensal").dataset.valores.split(",").map(parseFloat),
                backgroundColor: "#f1c40f",
                borderColor: "#f39c12",
                fill: false
            }]
        },
        options: { responsive: true }
    });

    // Gráfico de Salários por Funcionário
    var ctxSalarios = document.getElementById("graficoSalarios").getContext("2d");
    new Chart(ctxSalarios, {
        type: "bar",
        data: {
            labels: document.getElementById("graficoSalarios").dataset.funcionarios.split(","),
            datasets: [{
                label: "Salários dos Funcionários (R$)",
                data: document.getElementById("graficoSalarios").dataset.salarios.split(",").map(parseFloat),
                backgroundColor: "#2ecc71"
            }]
        },
        options: { responsive: true }
    });
});

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
                    document.getElementById("graficoFinanceiro").dataset.salarios,
                    document.getElementById("graficoFinanceiro").dataset.pagamentos
                ],
                backgroundColor: ["#3498db", "#e74c3c"]
            }]
        }
    });

    // Variáveis dos elementos
    var btnMensal = document.getElementById("btnMostrarGraficoMensal");
    var containerMensal = document.getElementById("graficoMensalContainer");
    var ctxMensal = document.getElementById("graficoMensal").getContext("2d");
    var chartMensal = null;

    // Alternar exibição do gráfico mensal
    btnMensal.addEventListener("click", function () {
        if (containerMensal.style.display === "none" || containerMensal.style.display === "") {
            containerMensal.style.display = "block";
            if (!chartMensal) {
                chartMensal = new Chart(ctxMensal, {
                    type: "line",
                    data: {
                        labels: document.getElementById("graficoMensal").dataset.meses.split(","),
                        datasets: [{
                            label: "Pagamentos Mensais (R$)",
                            data: document.getElementById("graficoMensal").dataset.valores.split(","),
                            backgroundColor: "#f1c40f",
                            borderColor: "#f39c12",
                            fill: false
                        }]
                    }
                });
            }
        } else {
            containerMensal.style.display = "none";
        }
    });

    // Variáveis dos elementos do gráfico de salários
    var btnSalarios = document.getElementById("btnMostrarGraficoSalarios");
    var containerSalarios = document.getElementById("graficoSalariosContainer");
    var ctxSalarios = document.getElementById("graficoSalarios").getContext("2d");
    var chartSalarios = null;

    // Alternar exibição do gráfico de salários
    btnSalarios.addEventListener("click", function () {
        if (containerSalarios.style.display === "none" || containerSalarios.style.display === "") {
            containerSalarios.style.display = "block";
            if (!chartSalarios) {
                chartSalarios = new Chart(ctxSalarios, {
                    type: "bar",
                    data: {
                        labels: document.getElementById("graficoSalarios").dataset.funcionarios.split(","),
                        datasets: [{
                            label: "Salários dos Funcionários (R$)",
                            data: document.getElementById("graficoSalarios").dataset.salarios.split(","),
                            backgroundColor: "#2ecc71"
                        }]
                    }
                });
            }
        } else {
            containerSalarios.style.display = "none";
        }
    });

});
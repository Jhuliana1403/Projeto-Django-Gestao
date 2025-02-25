document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("produtor").addEventListener("change", function () {
        var produtorId = this.value;
        var coletaSelect = document.getElementById("coleta");

        coletaSelect.innerHTML = '<option value="">Selecione a Coleta</option>';

        if (produtorId) {
            fetch(`/obter_coletas/?produtor_id=${produtorId}`)
                .then(response => {
                    if (!response.ok) {
                        return response.json().then(error => { throw new Error(error.error); });
                    }
                    return response.json();
                })
                .then(data => {
                    data.forEach(coleta => {
                        var option = document.createElement("option");
                        option.value = coleta.id;
                        option.textContent = `${coleta.quantidade_litros} Litros`;
                        coletaSelect.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error('Erro ao buscar coletas:', error);
                    alert(error.message);
                });
        }
    });
});

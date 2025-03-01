// Função para mostrar/ocultar o campo de motivo de atraso com base no status
function toggleMotivoAtraso() {
    var status = document.getElementById('status').value;
    var motivoAtrasoContainer = document.getElementById('motivo_atraso_container');
    
    if (status === 'Atraso') {
        motivoAtrasoContainer.style.display = 'block';
    } else {
        motivoAtrasoContainer.style.display = 'none';
    }
}

// Inicializa o estado do motivo de atraso quando a página carrega
document.addEventListener("DOMContentLoaded", function() {
    toggleMotivoAtraso();
});

// Adiciona um ouvinte de evento para alterar a visibilidade quando o status mudar
document.getElementById('status').addEventListener('change', function() {
    toggleMotivoAtraso();
});

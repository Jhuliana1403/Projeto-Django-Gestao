from django.db import models

class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    fazenda = models.CharField(max_length=150)
    localizacao = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)  # Campo para verificar se o produtor está ativo

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


from django.db import models

class Coleta(models.Model):
    produtor = models.ForeignKey('Produtor', on_delete=models.CASCADE)
    data = models.DateField()  # Agora o usuário pode escolher a data no formulário
    quantidade_litros = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produtor.nome} - {self.quantidade_litros}L"


class Qualidade(models.Model):
    coleta = models.OneToOneField(Coleta, on_delete=models.CASCADE)
    gordura = models.DecimalField(max_digits=5, decimal_places=2)
    proteina = models.DecimalField(max_digits=5, decimal_places=2)
    contagem_bacteriana = models.IntegerField()
    STATUS_CHOICES = [('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Qualidade - {self.coleta.produtor.nome}"


class Pagamento(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)
    data_pagamento = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    METODO_CHOICES = [('Pix', 'Pix'), ('Boleto', 'Boleto'), ('Transferência', 'Transferência')]
    metodo_pagamento = models.CharField(max_length=15, choices=METODO_CHOICES)

    def __str__(self):
        return f"Pagamento {self.produtor.nome} - R$ {self.valor}"


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(auto_now_add=True)
    quantidade_litros = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda {self.cliente.nome} - {self.quantidade_litros}L"


# class Transporte(models.Model):
#     venda = models.OneToOneField(Venda, on_delete=models.CASCADE)
#     motorista = models.CharField(max_length=100)
#     placa_veiculo = models.CharField(max_length=20)
#     data_envio = models.DateTimeField()
#     data_entrega = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"Transporte para {self.venda.fornecedor.nome}"

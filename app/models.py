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

class Coleta(models.Model):
    produtor = models.ForeignKey('Produtor', on_delete=models.CASCADE)
    data = models.DateField()  # Agora o usuário pode escolher a data no formulário
    quantidade_litros = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produtor.nome} - {self.quantidade_litros}L"


class Qualidade(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)  
    coleta = models.OneToOneField(Coleta, on_delete=models.CASCADE)
    gordura = models.DecimalField(max_digits=5, decimal_places=2)
    proteina = models.DecimalField(max_digits=5, decimal_places=2)
    contagem_bacteriana = models.IntegerField()
    status = models.CharField(
        max_length=50, 
        choices=[("Aprovado", "Aprovado"), ("Reprovado", "Reprovado")], 
        null=False, 
        blank=False,  # Garante que o campo não pode ficar vazio
        default="Aprovado"  # Adiciona um valor padrão para evitar erros
    )
    ativo = models.BooleanField(default = True)


    def __str__(self):
        return f"Qualidade - {self.coleta.produtor.nome}"


class Pagamento(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)
    data_pagamento = models.DateField(blank=True, null=True)  # Agora a data pode ser inserida manualmente
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    METODO_CHOICES = [
        ('Pix', 'Pix'),
        ('Boleto', 'Boleto'),
        ('Transferência', 'Transferência'),
    ]
    metodo_pagamento = models.CharField(max_length=15, choices=METODO_CHOICES)

    def __str__(self):
        return f"Pagamento {self.produtor.nome} - R$ {self.valor}"

class Funcionario(models.Model):
    imagem = models.ImageField(upload_to='funcionarios/', blank=True, null=True)
    nome = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    funcao = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    imagem = models.ImageField(upload_to='vendas/', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(auto_now_add=True)
    quantidade_litros = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda {self.cliente.nome} - {self.quantidade_litros}L"
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_inicial = models.IntegerField()
    quantidade_final = models.IntegerField()

    def diferenca_quantidade(self):
        return self.quantidade_inicial - self.quantidade_final

    def save(self, *args, **kwargs):
        # Sempre que um produto for salvo, atualizamos o financeiro
        super().save(*args, **kwargs)
        FluxoCaixa.atualizar_fluxo(self)

class FluxoCaixa(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    diferenca_quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def atualizar_fluxo(cls, produto):
        diferenca = produto.diferenca_quantidade()
        valor_total = diferenca * produto.valor
        fluxo, created = cls.objects.update_or_create(
            produto=produto,
            defaults={"diferenca_quantidade": diferenca, "valor_total": valor_total},
        )
        return fluxo

from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.data)

    @property
    def total(self):
        total = 0
        for item in self.items.all():
            total += item.produto.preco * item.quantidade
        return total


class ItemVenda(models.Model):
    quantidade = models.PositiveIntegerField(default=0,)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='vendas', )
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return 'Venda em' + str(self.venda.data)

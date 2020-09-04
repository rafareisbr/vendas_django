from django.db import models

from .choices import \
    PAGAMENTO_CHOICES, VENDA_STATUS_CHOICES, \
    VENDA_AGUARDANDO_PAGAMENTO, VENDA_PAGAMENTO_CONFIRMADO
from core.models import TimeStampedModel


class Produto(TimeStampedModel):
    nome = models.CharField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Venda(TimeStampedModel):
    status = models.CharField(
        max_length=4,
        choices=VENDA_STATUS_CHOICES,
        default=VENDA_AGUARDANDO_PAGAMENTO
    )

    def __str__(self):
        return str(self.created.strftime('%m/%d/%Y às %H:%M:%S'))

    @property
    def total(self):
        total = 0
        for item in self.items.all():
            total += item.produto.preco * item.quantidade
        return total

    def pagar(self):
        self.status = VENDA_PAGAMENTO_CONFIRMADO
        return self


class ItemVenda(TimeStampedModel):
    quantidade = models.PositiveIntegerField(default=0,)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='vendas', )
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return 'Venda em' + str(self.venda.created)


class Pagamento(TimeStampedModel):
    venda = models.OneToOneField(
        to=Venda,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return 'Pagamento da venda: ' + str(self.venda.id)


class ItemPagamento(TimeStampedModel):
    opcao = models.CharField(max_length=4, choices=PAGAMENTO_CHOICES,)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    pagamento = models.ForeignKey(to=Pagamento, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return 'Opcao: ' + str(self.get_opcao_display()) + ' Valor: ' + str(self.valor)
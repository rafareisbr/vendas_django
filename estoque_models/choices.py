DINHEIRO = 'DINH'
CARTAO_DE_DEBITO = 'CDEB'
CARTAO_DE_CREDITO = 'CCRE'
BOLETO = 'BLTO'

PAGAMENTO_CHOICES = [
    (DINHEIRO, 'Dinheiro'),
    (CARTAO_DE_DEBITO, 'Cartão de Débito'),
    (CARTAO_DE_CREDITO, 'Cartão de Crédito'),
    (BOLETO, 'Boleto')
]

# Status de uma venda
VENDA_AGUARDANDO_PAGAMENTO = 'AGPG'
VENDA_PAGAMENTO_CONFIRMADO = 'PGCF'

VENDA_STATUS_CHOICES = [
    ('AGPG', 'Aguardando pagamento'),
    ('PGCF', 'Pagamento confirmado')
]
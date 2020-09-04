from django.contrib import admin

from estoque_models.models import Produto, ItemVenda, Venda, Pagamento, ItemPagamento


class ItemVendaInline(admin.StackedInline):
    model = ItemVenda
    extra = 3


class VendaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Detalhes da Venda', {'fields': ['data', 'status'], 'classes': ['collapse']})
    ]
    inlines = [ItemVendaInline]
    readonly_fields = ['data']


class ItemPagamentoInline(admin.StackedInline):
    model = ItemPagamento
    extra = 3


class PagamentoAdmin(admin.ModelAdmin):
    inlines = [ItemPagamentoInline]


admin.site.register(Produto)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Pagamento, PagamentoAdmin)


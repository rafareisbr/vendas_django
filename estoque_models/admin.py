from django.contrib import admin

from estoque_models.models import Produto, ItemVenda, Venda, Pagamento


class ItemVendaInline(admin.StackedInline):
    model = ItemVenda
    extra = 3


class VendaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Detalhes da Venda', {'fields': ['data', 'status'], 'classes': ['collapse']})
    ]
    inlines = [ItemVendaInline]
    readonly_fields = ['data']


admin.site.register(Produto)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Pagamento)


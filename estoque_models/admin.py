from django.contrib import admin

# Register your models here.
from estoque_models.models import Produto, ItemVenda, Venda


class ItemVendaInline(admin.StackedInline):
    model = ItemVenda
    extra = 3


class VendaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data da Venda', {'fields': ['data'], 'classes': ['collapse']})
    ]
    inlines = [ItemVendaInline]


admin.site.register(Produto)
admin.site.register(Venda, VendaAdmin)


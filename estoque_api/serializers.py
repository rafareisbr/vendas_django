from django.db import IntegrityError
from rest_framework import serializers

from estoque_models.models import Produto, Venda, ItemVenda, Pagamento


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


class ItemPagamentoSerializer(serializers.ModelSerializer):
    opcao = serializers.SerializerMethodField()

    class Meta:
        model = ItemVenda
        fields = '__all__'

    def get_opcao(self, instance):
        return instance.get_opcao_display()


class PagamentosSerializer(serializers.ModelSerializer):
    items = ItemPagamentoSerializer(many=True)

    class Meta:
        model = Pagamento
        fields = '__all__'

    def validar_valor_total(self, items):
        # if len(attrs) == 0:
        #     raise serializers.ValidationError({"field": "items", "error": "Precisa ter pelo menos um item na venda."})
        total = 0.0
        for item in items:
            total += item.valor
        print(total)

    def create(self, validated_data):

        items_data = validated_data.pop('items')
        if self.validar_valor_total(items_data):
            return items_data


class ItemVendaSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    venda = serializers.IntegerField(write_only=True)

    class Meta:
        model = ItemVenda
        fields = '__all__'
        # depth = 1


class VendasSerializer(serializers.ModelSerializer):
    items = ItemVendaSerializer(many=True)
    pagamento = PagamentosSerializer(many=False, required=False)
    total = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Venda
        fields = ['id', 'items', 'total', 'pagamento', 'status']
        read_only_fields = ['total', 'pagamento', 'status']

    def get_total(self, instance):
        return instance.total

    def get_status(self, instance):
        return instance.get_status_display()


class InsertItemVendaSerializer(serializers.Serializer):
    produto_id = serializers.IntegerField(min_value=1, max_value=100, required=True)
    quantidade = serializers.IntegerField(min_value=1, max_value=100, required=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class InsertVendasSerializer(serializers.ModelSerializer):
    items = InsertItemVendaSerializer(many=True, required=True)

    class Meta:
        model = Venda
        fields = '__all__'

    @staticmethod
    def validar_tem_item_no_carrinho(attrs):
        if len(attrs) == 0:
            raise serializers.ValidationError({"campo": "items", "mensagem": "Precisa ter pelo menos um item na venda."})
        return attrs

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        if self.validar_tem_item_no_carrinho(items_data):
            venda = Venda.objects.create()
            for item_data in items_data:
                try:
                    ItemVenda.objects.create(**item_data, venda_id=venda.id)
                except IntegrityError:
                    raise serializers.ValidationError({"mensagem": "Algum dos ids enviados não existe na base de dados."})
            return venda

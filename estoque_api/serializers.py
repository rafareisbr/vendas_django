from django.db import IntegrityError
from rest_framework import serializers

from estoque_models.models import Produto, Venda, ItemVenda


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


class ItemVendaSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    venda = serializers.IntegerField(write_only=True)

    class Meta:
        model = ItemVenda
        fields = '__all__'
        # depth = 1


class VendasSerializer(serializers.ModelSerializer):
    items = ItemVendaSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Venda
        fields = ['items', 'total']
        read_only_fields = ['total']

    def get_total(self, instance):
        return instance.total


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
    def validate_at_least_one_item(attrs):
        if len(attrs) == 0:
            raise serializers.ValidationError({"field": "items", "error": "Precisa ter pelo menos um item na venda."})
        return attrs

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        if self.validate_at_least_one_item(items_data):
            venda = Venda.objects.create()
            for item_data in items_data:
                try:
                    ItemVenda.objects.create(**item_data, venda_id=venda.id)
                except IntegrityError:
                    raise serializers.ValidationError({"error": "Algum dos ids enviados não existe na base de dados."})
            return venda



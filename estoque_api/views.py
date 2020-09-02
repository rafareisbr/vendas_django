import json

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from estoque_api.serializers import ProdutoSerializer, VendasSerializer,\
    InsertVendasSerializer, PagamentosSerializer

from estoque_models.models import Produto, Venda, Pagamento


class ProdutosViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class VendasViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendasSerializer

    def create(self, request):
        serializer = InsertVendasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PagamentosViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):

    queryset = Pagamento.objects.all()
    serializer_class = PagamentosSerializer

from django.urls import include, path

from rest_framework.routers import DefaultRouter

from estoque_api.views import ProdutosViewSet, VendasViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutosViewSet)
router.register(r'vendas', VendasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

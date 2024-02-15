from django.urls import path
from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, sample_view

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls + [path('test/', sample_view, name='test')]

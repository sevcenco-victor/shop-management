from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (CategoryViewSet, ProductViewSet,
                    OrderViewSet, PaymentViewSet)

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet, basename='orders')
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = []

urlpatterns += router.urls

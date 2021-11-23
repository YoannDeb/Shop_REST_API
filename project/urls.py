from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.views import CategoryViewSet, ProductViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))
]

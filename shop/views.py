from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.models import Category, Product, Article
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer


class CategoryViewSet(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()

        if self.request.GET.get('show_inactive') != 'true':
            queryset = queryset.filter(active=True)

        return queryset


class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        if self.request.GET.get('show_inactive') != 'true':
            queryset = queryset.filter(active=True)

        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset


class ArticleViewSet(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):

        queryset = Article.objects.all()

        if self.request.GET.get('show_inactive') != 'true':
            queryset = queryset.filter(active=True)

        product_id = self.request.GET.get('product_id')
        if product_id:
            queryset = queryset.filter(product_id=product_id)

        return queryset



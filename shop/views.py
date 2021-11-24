from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from shop.models import Category, Product, Article
from shop.serializers import CategoryListSerializer, CategoryDetailSerializer, ProductListSerializer, ProductDetailSerializer, ArticleSerializer


class CategoryViewSet(ReadOnlyModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        if self.request.GET.get('show_inactive') != 'true':
            queryset = queryset.filter(active=True)
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.GET.get('show_inactive') != 'true':
            queryset = queryset.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


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



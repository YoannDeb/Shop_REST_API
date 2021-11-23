from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


# class ProductAPIView(APIView):
#
#     def get(selfself, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

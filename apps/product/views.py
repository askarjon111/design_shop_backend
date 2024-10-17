from rest_framework.generics import ListAPIView

from apps.product.models import Category
from apps.product.serializers import CategorySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.product.models import Category, Event
from apps.product.serializers import CategorySerializer, EventSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def events_view(request):
    category_name = request.GET.get('category')
    category = Category.objects.filter(name=category_name).last()
    events = Event.objects.filter(category=category)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

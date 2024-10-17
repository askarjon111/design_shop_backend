from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.main.models import Customer
from apps.main.serializers import CustomerSerializer


class CustomerRegisterView(CreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer


@api_view(['GET'])
def get_customer_view(request):
    telegram_id = request.GET.get('telegram_id')
    customer = Customer.objects.filter(telegram_id=telegram_id)
    if customer:
        customer = CustomerSerializer(customer.last()).data
        return Response({'customer': customer})
    else:
        return Response({}, 404)

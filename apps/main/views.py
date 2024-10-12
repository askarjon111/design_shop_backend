from rest_framework.generics import CreateAPIView

from apps.main.models import Customer
from apps.main.serializers import CustomerSerializer


class CustomerRegisterView(CreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer

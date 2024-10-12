from django.urls import path

from apps.main.views import CustomerRegisterView, get_customer_view


urlpatterns = [
    path('customer/create/', CustomerRegisterView.as_view(), name='register'),
    path('customer/', get_customer_view, name='get_customer'),
]


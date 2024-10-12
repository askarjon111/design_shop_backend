from django.urls import path

from apps.main.views import CustomerRegisterView


urlpatterns = [
    path('customer/create/', CustomerRegisterView.as_view(), name='register'),
]


from django.urls import path

from apps.product.views import CategoryListView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
]

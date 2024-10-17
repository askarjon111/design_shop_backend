from django.urls import path

from apps.product.views import CategoryListView, events_view


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('events/', events_view, name='events'),
]

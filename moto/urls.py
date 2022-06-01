from django.urls import path
from .views import MotoList, MotoDetail


urlpatterns = [
    path('', MotoList.as_view(), name='moto_list'),
    path('<int:pk>/', MotoDetail.as_view(), name='moto_detail'),
]

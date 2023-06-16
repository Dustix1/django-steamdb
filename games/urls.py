from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kategorie/<int:pk>', views.category_detail, name='category_detail'),
    path('<int:pk>', views.HraDetailView.as_view(), name='game_detail'),
    path('vyvojar/<int:pk>', views.VyvojarDetailView.as_view(), name='developer_detail'),
]
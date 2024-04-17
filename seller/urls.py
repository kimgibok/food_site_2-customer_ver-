from django.urls import path
from . import views

app_name='seller'
urlpatterns = [
    path('', views.seller_index, name='seller_index'),
    path('add_item/', views.add_item, name='add_item'),
    path('item_detail/<int:pk>/', views.item_detail, name='item_detail'),
    path('item_delete/<int:pk>/', views.item_delete, name='item_delete'),
]
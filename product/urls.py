from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('detail/<int:product_id>', views.detail, name='detail'),
    path('upvote/<int:product_id>', views.upvote, name='upvote'),
]

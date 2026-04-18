from django.urls import path
from main.views import index, shop, product

urlpatterns = [
  path('', index, name='index'),
  path('shop/', shop, name='shop'),
  path('product/<int:id>/', product, name='product'),
]
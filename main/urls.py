from django.urls import path
from main.views import index, shop, product, product_info,new

urlpatterns = [
  path('', index, name='index'),
  path('shop/', shop, name='shop'),
  path('product/<int:id>/', product, name='product'),
  path('product_info/<int:id>/', product_info, name='product_info'),
  path('new/', new, name='new'),
]
from django.urls import path
from . import  views


urlpatterns = [
    path('get-products/',views.get_products),
    path('products',views.products_view,name='product'),
    path('products/<int:pk>',views.view_single_product,name='single_product')
]
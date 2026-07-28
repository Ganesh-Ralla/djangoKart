from django.urls import path
from . import  views


urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.get_products,name='home'),
    path('products',views.products_view,name='product'),
    path('products/<int:pk>',views.view_single_product,name='single_product')
]
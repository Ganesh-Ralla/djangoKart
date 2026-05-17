from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    
    path('products/<int:pk>',views.view_single_product,name='single_product'),
    path('view-order/<int:pk>',views.view_Order,name='view_order'),

]
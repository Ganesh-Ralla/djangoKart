from django.shortcuts import render, redirect
from cart.models import cart
from .models import Order,OrderItems
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def place_order(request):

    cart_items = cart.objects.filter(user = request.user)

    total_price = 0

    for item in cart_items:
        sub_total = (item.products.price*item.quantity)
        total_price+=sub_total


    order = Order.objects.create(
        user = request.user,
        total_price = total_price
    )

    for item in cart_items:
        orderItem = OrderItems.objects.create(
            order=order,
            product = item.products,
            quantity = item.quantity
        )

    cart_items.delete()
    return redirect('home')


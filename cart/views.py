from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import cart
from products.models import Product


# Create your views here.
@login_required
def cart_view(request):
    cart_items = cart.objects.filter(user=request.user)

    total_price = 0
    items_count = 0
    for item in cart_items:
        item.sub_total = (item.products.price * item.quantity)
        total_price+=item.sub_total
        items_count += item.quantity
    context = {
        'cart_items': cart_items,
        'total_price' : total_price,
        'items_count':items_count
    }

    return render(request,'cart.html',context)

@login_required
def add_to_cart(request,pk):
    product = Product.objects.get(pk=pk)

    cart_item = cart.objects.filter(
        user=request.user,
        products = product
    )

    if cart_item:
        item = cart_item.first()
        item.quantity += 1
        item.save()
    else:
        cart.objects.create(
            user = request.user,
            products=product
        )
    return redirect('product')


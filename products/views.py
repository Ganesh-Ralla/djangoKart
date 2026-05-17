from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import requests


# Create your views here.
def get_products(request):

    url = "https://dummyjson.com/products?limit=100"

    response = requests.get(url)
    data = response.json()

    products = data['products']

    for item in products:
        Product.objects.create(
            title=item.get('title', ''),
            description=item.get('description', ''),
            category=item.get('category', ''),
            brand=item.get('brand', ''),
            price=item.get('price', 0),
            discount_percentage=item.get('discountPercentage', 0),
            rating=item.get('rating', 0),
            stock=item.get('stock', 0),
            thumbnail=item.get('thumbnail', ''),
            sku=item.get('sku', ''),
            warranty_information=item.get('warrantyInformation', ''),
            shipping_information=item.get('shippingInformation', ''),
            availability_status=item.get('availabilityStatus', ''),
            return_policy=item.get('returnPolicy', ''),
            minimum_order_quantity=item.get('minimumOrderQuantity', 0)
        )

    return HttpResponse("Products Saved")


def products_view(request):
    products = Product.objects.all()


    return render(request, 'products.html', {'products': products})

def view_single_product(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'singleproduct.html',{'product':product})
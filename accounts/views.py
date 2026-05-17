from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from products.models import Product
from orders.models import OrderItems,Order

# Create your views here.
def home(request):
    products = Product.objects.all()[80:90]
    return render(request,'index.html',{'products':products})

def register(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request,'register.html',{'form': form })
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
    else:
        return render(request,'login.html')
    return render(request,'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')

def profile(request):
    user = request.user
    orders = Order.objects.filter(user = request.user)
    context={
        'user': user,
        'orders':orders
    }
    return render(request,'profile.html',context)

def view_single_product(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'singleproduct.html',{'product':product})

def view_Order(request,pk):
    order = Order.objects.get(pk=pk)
    # orderItems = OrderItems.objects.filter(order=order)
    context = {
        'orders':order,
        # 'orderItems':orderItems,
    }
    return render(request,'orders.html',context)
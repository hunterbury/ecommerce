from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import *
import json
import datetime
from .utils import cookieCart, cartData, guestOrder
from .filters import ProductFilter
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = filter.qs

    context = {'products':products, 'cartItems':cartItems, 'filter': filter}

    if request.user.is_authenticated:
        return render(request, 'store/home.html', context)
    else:
        return redirect('/login/')

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def demoLogin(request):
    if request.method == 'POST':
        username = 'demo_user'
        password = 'demo_password'
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('/')

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = filter.qs

    paginator = Paginator(products, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products':products, 'cartItems':cartItems, 'filter': filter, 'page_obj':page_obj}
    return render(request, 'store/store.html', context)

def productInfo(request, pk):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    product = Product.objects.get(id=pk)
    photos = ProductImage.objects.filter(product=product)
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = Product.objects.all()

    context = {'items':items, 'order':order, 'cartItems':cartItems, 'product':product, 'photos':photos, 'filter': filter, 'products': products}
    return render(request, 'store/product.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    filter = ProductFilter(request.GET, queryset=Product.objects.all())

    context = {'items':items, 'order':order, 'cartItems':cartItems, 'filter': filter}
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    filter = ProductFilter(request.GET, queryset=Product.objects.all())

    context = {'items':items, 'order':order, 'cartItems':cartItems, 'filter': filter}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete', safe=False)

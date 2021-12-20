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

def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = filter.qs

    context = {'products':products, 'cartItems':cartItems, 'filter': filter}
    return render(request, 'store/home.html', context)

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = filter.qs

    paginator = Paginator(products, 15)

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

    context = {'items':items, 'order':order, 'cartItems':cartItems, 'product':product, 'photos':photos, 'filter': filter}
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

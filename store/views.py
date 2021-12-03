from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import *
import json
import datetime
from .utils import cookieCart, cartData, guestOrder
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

@api_view(['GET'])
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    query = request.GET.get('q', None)
    if query:
        products = products.filter(
            Q(name__icontains=query)
    )

    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

@api_view(['GET'])
def productInfo(request, pk):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/product.html', context)

@api_view(['GET'])
def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


# def store(request):
#     data = cartData(request)
#     cartItems = data['cartItems']

#     products = Product.objects.all()
#     query = request.GET.get('q', None)
#     if query:
#         products = products.filter(
#             Q(name__icontains=query)
#         )
#     context = {'products':products, 'cartItems':cartItems}
#     return render(request, 'store/store.html', context)

# def productInfo(request):
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']

#     context = {'items':items, 'order':order, 'cartItems':cartItems}
#     return render(request, 'store/product.html', context)

# def cart(request):
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']

#     context = {'items':items, 'order':order, 'cartItems':cartItems}
#     return render(request, 'store/cart.html', context)

# def checkout(request):
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']

#     context = {'items':items, 'order':order, 'cartItems':cartItems}
#     return render(request, 'store/checkout.html', context)

# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']

#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)

#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#     if action == 'add':
#         orderItem.quantity = orderItem.quantity + 1
#     elif action == 'remove':
#         orderItem.quantity = orderItem.quantity - 1

#     orderItem.save()

#     if orderItem.quantity <= 0:
#         orderItem.delete()

#     return JsonResponse('Item was added', safe=False)

# def processOrder(request):
#     transaction_id = datetime.datetime.now().timestamp()
#     data = json.loads(request.body)

#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)

#     else:
#         customer, order = guestOrder(request, data)

#     total = float(data['form']['total'])
#     order.transaction_id = transaction_id

#     if total == order.get_cart_total:
#         order.complete = True
#     order.save()

#     if order.shipping == True:
#         ShippingAddress.objects.create(
#             customer = customer,
#             order = order,
#             address = data['shipping']['address'],
#             city = data['shipping']['city'],
#             state = data['shipping']['state'],
#             zipcode = data['shipping']['zipcode'],
#         )

#     return JsonResponse('Payment complete', safe=False)

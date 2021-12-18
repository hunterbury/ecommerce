from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
path('', views.home, name="home"),
path('store/', views.store, name="store"),
path('cart/', views.cart, name="cart"),
path('checkout/', views.checkout, name="checkout"),
path('update-item/', views.updateItem, name="update-item"),
path('process-order/', views.processOrder, name="process-order"),
path('product-info/<str:pk>/', views.productInfo, name="product-info"),
]
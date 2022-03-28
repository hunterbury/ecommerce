from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
path('', views.home, name="home"),
# path('login/', views.loginView, name="login"),
# path('demo-login/', views.demoLogin, name="demo-login"),
path('', include('django.contrib.auth.urls')),
path('store/', views.store, name="store"),
path('cart/', views.cart, name="cart"),
path('checkout/', views.checkout, name="checkout"),
path('update-item/', views.updateItem, name="update-item"),
path('process-order/', views.processOrder, name="process-order"),
path('product-info/<str:pk>/', views.productInfo, name="product-info"),
]
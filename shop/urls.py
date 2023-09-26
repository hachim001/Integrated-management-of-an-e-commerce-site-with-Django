
from django.urls import path
from . import views

urlpatterns = [
path('shop/', views.shop, name='shop'),
path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),]
from django.urls import path
from cart import views
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('cart/delete/<int:cart_item_id>/', views.delete_cart, name='delete_cart_item'),
    path('login/',views.login_view,name='login')
]
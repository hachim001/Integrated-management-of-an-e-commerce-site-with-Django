from django.shortcuts import render
from .models import Product , Category
from cart.models import Cart



# Create your views here.
def index(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
      cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = None
    context={
        'products':products,
        'cart_items': cart_items
        
    }
   
    return render(request,'index.html',context)
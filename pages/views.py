from django.shortcuts import render
from cart.models import Cart

def blog(request):
    if request.user.is_authenticated:
      cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = None
    return render(request, 'blog.html', {'cart_items': cart_items})


# Create your views here.

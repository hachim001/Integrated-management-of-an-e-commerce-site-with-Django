from django.shortcuts import render
from product import models
from product.models import Product, Category
from django.core.paginator import Paginator
from django.db.models import Q
from cart.models import Cart

def shop(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    products = Product.objects.all()
    categories = Category.objects.all()
    marque = request.GET.get('marque')
    if request.user.is_authenticated:
       cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = None

    if query:
        products = products.filter(
            Q(title__icontains=query) | 
            Q(marque__icontains=query) |
            Q(description__icontains=query)
        )
    if category:
        products = products.filter(category__name__icontains=category)
    if marque:
        products = products.filter(marque__icontains=marque)    

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'pages': paginator.page_range,
        'categories': categories,
        'cart_items': cart_items

    }

    return render(request, 'shop.html', context)


from django.views.generic import DetailView
class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['size_range'] = range(38, 44)  
        return context
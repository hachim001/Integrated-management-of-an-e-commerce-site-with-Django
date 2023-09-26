from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from cart.models import Cart
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from account.forms import loginForm


def add_to_cart(request, product_id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))

        # Valider la quantité
        if quantity <= 0:
            messages.error(request, 'Invalid quantity. Please enter a positive value.')
            return redirect('product_detail', product_id=product_id)

        # Récupérer le produit
        product = get_object_or_404(Product, pk=product_id)

        if request.user.is_authenticated:
            # L'utilisateur est authentifié, ajouter au panier de l'utilisateur
            cart_item = Cart.objects.filter(user=request.user, product=product, size=size).first()

            if cart_item:
                # Un élément de panier avec le même produit et la même taille existe déjà, incrémenter la quantité
                cart_item.quantity += quantity
            else:
                # Créer un nouvel objet Cart
                cart_item = Cart(user=request.user, product=product, size=size, quantity=quantity)

            cart_item.subtotal = cart_item.product.price * cart_item.quantity
            cart_item.save()

            messages.success(request, 'Product added to cart successfully.')
        else:
            # L'utilisateur n'est pas authentifié, stocker temporairement les informations du produit dans la session
            cart_item_data = {
                'product_id': product.id,
                'size': size,
                'quantity': quantity,
            }
            request.session.setdefault('cart_items', []).append(cart_item_data)

        return redirect('cart')

    # Gérer les cas où la méthode de requête n'est pas POST
    return redirect('product_detail', product_id=product_id)


@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        # Récupérer les éléments du panier de l'utilisateur authentifié
        cart_items = Cart.objects.filter(user=request.user)
    else:
        # Récupérer les éléments du panier à partir de la session
        cart_items_data = request.session.get('cart_items', [])
        
        cart_items = []
        for cart_item_data in cart_items_data:
            product = get_object_or_404(Product, pk=cart_item_data['product_id'])
            cart_item = Cart(product=product, size=cart_item_data['size'], quantity=cart_item_data['quantity'])
            cart_items.append(cart_item)

    context = {
        'cart_items': cart_items
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def delete_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    cart_item.delete()
    messages.success(request, 'Product removed from cart successfully.')
    return redirect('cart')


def login_view(request):
    messages.get_messages(request)
    form = loginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if 'cart_items' in request.session:
                cart_items_data = request.session.pop('cart_items')
                for cart_item_data in cart_items_data:
                    product = get_object_or_404(Product, pk=cart_item_data['product_id'])
                    cart_item = Cart(user=request.user, product=product, size=cart_item_data['size'], quantity=cart_item_data['quantity'])
                    cart_item.subtotal = cart_item.product.price * cart_item.quantity
                    cart_item.save()

            return redirect('cart')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'account/login.html', {'form': form})
def update_cart(request, cart_item_id):
    if request.method == 'POST':
        cart_item = Cart.objects.get(pk=cart_item_id)
        quantity = int(request.POST.get('quantity'))

        # Perform additional validations or checks
        if quantity <= 0:
            messages.error(request, 'Invalid quantity. Please enter a positive value.')
            return redirect('cart')

        cart_item.quantity = quantity
        cart_item.subtotal = cart_item.product.price * quantity
        cart_item.save()

        messages.success(request, 'Cart updated successfully.')
        return redirect('cart')
def quantite_total(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items
    }
    return render(request, 'base.html', context)



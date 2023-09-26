from django.contrib import admin
from .models import Cart

class AdminCart(admin.ModelAdmin):
    list_display = ('user', 'product','quantity','size','subtotal')
    fields = ('user', 'product','quantity','size')
    
    

admin.site.register(Cart,AdminCart)


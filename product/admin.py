from django.contrib import admin
from .models import Category , Product 

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_creation')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price','marque','category','date_creation','product_image')

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)

from django.contrib import admin
from .models import Category, Product, Contact, Profile, Cart, CartItem

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    prepopulated_fields = {'slug' : ('cat_name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category')
    prepopulated_fields = {'slug' : ('product_name',)}
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItem)

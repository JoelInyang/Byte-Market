from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField(max_length=100, blank=True)
    cat_image = models.ImageField(upload_to='photos/category', blank=True)
    
    def __str__(self):
        return self.cat_name


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=200, blank=True, default=" ● 'description'. ● 'description'. ● 'description'. ")
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/product', blank=True)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    number = models.IntegerField()
    subject = models.TextField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    #lastname = models.CharField(max_length=50)
    img = models.ImageField(upload_to='profile_img')
    email = models.EmailField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username.username
    
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product.product_name
    
    
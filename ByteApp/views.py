from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Contact, Profile, Cart, CartItem
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request, cat_slug=None):
    categories = None
    products = None
    
    if cat_slug != None:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all().filter().order_by('id')
    
    context = {
        'products' : products,
    }
    return render(request, 'index.html', context)
def fashion_child_product(request, cat_slug=None):
    categories = None
    products = None
    
    if cat_slug != None:
        categories= get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
        
    else:
        products = Product.objects.all().filter().order_by('id')
    
    context = {
        'products' : products,
        'categories' : categories,
    }
    
    return render(request, 'fashion-child-product.html', context)
def laptop_product(request, cat_slug=None):
    
    categories = None
    products = None
    
    if cat_slug != None:
        categories= get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all().filter().order_by('id')
    
    
    context = {
        'products' : products,
        'categories' : categories,
    }
    
    return render(request, 'laptop-product.html', context)
def footwear_product(request, cat_slug=None):
    
    categories = None
    products = None
    
    if cat_slug != None:
        categories= get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all().filter().order_by('id')
    
    
    context = {
        'products' : products,
        'categories' : categories,
    }
    
    return render(request, 'footwear-product.html', context)
def gift_product(request, cat_slug=None):
    
    categories = None
    products = None
    
    if cat_slug != None:
        categories= get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all().filter().order_by('id')
    
    
    context = {
        'products' : products,
        'categories' : categories,
    }
    
    return render(request, 'gift-product.html', context)
def phone_product(request, cat_slug=None):
    
    categories = None
    products = None
    
    if cat_slug != None:
        categories= get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all().filter().order_by('id')
    
    
    context = {
        'products' : products,
        'categories' : categories,
    }
    
    return render(request, 'phone-product.html', context)
def toys_product(request, cat_slug=None):
    
    categories = None
    products = None
    
    if cat_slug != None:
        categories= get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all().filter().order_by('id')
    
    
    context = {
        'products' : products,
        'categories' : categories,
    }
    
    return render(request, 'toys-product.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='signin')
def cart(request):
    return render(request, 'cart.html')


#from django.contrib.auth.decorators import login_required
#from django.shortcuts import get_object_or_404


def account(request):
    #profile = Profile.objects.get(username=request.user)
    
    #context = {
   #     'profile': profile,
   # }
    
    return render(request, 'account.html')



"""@login_required(login_url='signin')
def product_detials_child(request, cat_slug=None):
    categories = None
    products = None
    
    if cat_slug != None:
        categories= get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
        
    else:
        products = Product.objects.all().filter().order_by('id')
    
    context = {
        'products' : products,
        'categories' : categories,
    }
    return render(request, 'product-detials-child2.html', context)
"""


"""
def product_detials_child(request, cat_slug=None, product_slug=None):
    categories = None
    products = None
    product = None
    
    
    if cat_slug is not None:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
        
        if product_slug is not None:
            product = get_object_or_404(Product, slug=product_slug, category=categories)
#            context = {
#                
#                'categories' : categories,
#            }
#            return render(request, 'product-details-child2.html', context)
        
    else:
        #products = Product.objects.all().order_by('id')
        products = Product.objects.filter(category__slug='child-clothes').order_by('id')
    
    
    paginator = Paginator(products, 2)  # Display 8 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'products': page_obj,
        'categories': categories,
        'product': product,
    }
    return render(request, 'product-detials-child2.html', context)
"""

def product_detials_child(request, cat_slug=None, product_slug=None):
    categories = None
    products = None
    product = None

    if cat_slug is not None:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)

        if product_slug is not None:
            product = get_object_or_404(Product, slug=product_slug, category=categories)

    else:
        products = Product.objects.filter(category__slug='child-clothes').order_by('id')

    paginator = Paginator(products, 4)  # Display 4 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    product_count = products.count()

    context = {
        'products': page_obj,
        'categories': categories,
        'product': product,
        'product_count' : product_count,
    }
    return render(request, 'product-detials-child2.html', context)


def product_detials_gift(request, cat_slug=None, product_slug=None):
    categories = None
    products = None
    product = None
    
    
    if cat_slug is not None:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
        
        if product_slug is not None:
            product = get_object_or_404(Product, slug=product_slug, category=categories)

        
    else:
        #products = Product.objects.all().order_by('id')
        products = Product.objects.filter(category__slug='gift').order_by('id')
    
    context = {
        'products': products,
        'categories': categories,
        'product': product,
    }
    return render(request, 'product-detials-gift.html', context)




def product_detials_footwear(request, cat_slug=None, product_slug=None):
    categories = None
    products = None
    product = None
    
    
    if cat_slug is not None:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
        
        if product_slug is not None:
            product = get_object_or_404(Product, slug=product_slug, category=categories)

        
    else:
        #products = Product.objects.all().order_by('id')
        products = Product.objects.filter(category__slug='footwear').order_by('id')
    
    context = {
        'products': products,
        'categories': categories,
        'product': product,
    }
    return render(request, 'product-detials-footwear.html', context)


def product_detials_toy(request):
    return render(request, 'product-detials-toy.html')


def product_detials_toy(request, cat_slug=None, product_slug=None):
    categories = None
    products = None
    product = None
    
    
    if cat_slug is not None:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
        
        if product_slug is not None:
            product = get_object_or_404(Product, slug=product_slug, category=categories)

        
    else:
        #products = Product.objects.all().order_by('id')
        products = Product.objects.filter(category__slug='toys').order_by('id')
    
    context = {
        'products': products,
        'categories': categories,
        'product': product,
    }
    return render(request, 'product-detials-toy.html', context)




def product_detials_laptop(request, cat_slug=None, product_slug=None):
    categories = None
    products = None
    product = None
    
    
    if cat_slug is not None:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
        
        if product_slug is not None:
            product = get_object_or_404(Product, slug=product_slug, category=categories)

        
    else:
        #products = Product.objects.all().order_by('id')
        products = Product.objects.filter(category__slug='laptop').order_by('id')
    
    context = {
        'products': products,
        'categories': categories,
        'product': product,
    }
    return render(request, 'product-detials-laptop.html', context)



def product_detials_phone(request, cat_slug=None, product_slug=None):
    categories = None
    products = None
    product = None
    
    
    if cat_slug is not None:
        categories = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=categories)
        
        if product_slug is not None:
            product = get_object_or_404(Product, slug=product_slug, category=categories)

        
    else:
        #products = Product.objects.all().order_by('id')
        products = Product.objects.filter(category__slug='phone').order_by('id')
    
    context = {
        'products': products,
        'categories': categories,
        'product': product,
    }
    return render(request, 'product-detials-phone.html', context)



@login_required(login_url='signin')
def contact_issue(request):
    if request.method == 'POST':
        name = request.POST.get('firstname')  # Access 'name' from the POST dictionary
        itemname = request.POST.get('item_name')  # Access 'item_name' from the POST dictionary
        number = request.POST.get('lastname')  # Access 'lastname' from the POST dictionary
        
        new_issue = Contact.objects.create(name=name, item_name=itemname, number=number)
        new_issue.save()
        return redirect('/contact')
    else:
        return redirect('/contact')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/account')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/account')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(username=user_model)
                new_profile.save()
                return redirect('/')
        else:
            messages.info(request, 'Password mismatch')
            return redirect('signup')
    else:
        return render(request, 'account.html')

def signin(request):
    #user_object = User.objects.get(username=request.user.username)
    #user_profile = Profile.objects.get(user=user_object)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user_login = auth.authenticate(username=username, password=password)
        if user_login is not None:
            auth.login(request, user_login)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        context = {
        }
        return render(request, 'account.html', context)
    

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


#def cart(request):
    cart = Cart.objects.all()
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    return render(request, 'cart.html')


@login_required(login_url='signin')
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_items = None
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_items = CartItem.objects.filter(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    
    context= {
        'cart_item' : cart_item,
        'cart' : cart,
        'cart_items' : cart_items,
    }
    return redirect('cart')
    #return render(request, 'cart.html', context)
    
    
"""    
def cart(request):
    cart_items=None
    #subtotal = 0
    delivery = 0
    total = 0
    quantity = 0
    
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        #cart = Cart.objects.all()
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            cart_item.subtotal = cart_item.product.price * cart_item.quantity
            #subtotal = cart_item.product.price
            total += cart_item.subtotal
            quantity += cart_item.quantity
            
        #tax = (2 * total)/100
        #grand_total = total + tax
        
        
    except ObjectDoesNotExist:
        pass
    
    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items': cart_items,
        #'subtotal' : subtotal,
    }
    return render(request, 'cart.html', context)
"""

#from django.shortcuts import redirect
@login_required(login_url='signin')
def cart(request):
    cart_items = None
    delivery = 0
    total = 0
    quantity = 0
    total_cost = 0
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
        if request.method == 'POST':
            for cart_item in cart_items:
                quantity = request.POST.get(f'quantity_{cart_item.id}', 0)
                cart_item.quantity = int(quantity)
                cart_item.save()
            
            return redirect('cart')  # Redirect to the cart page to see the updated quantities
        
        for cart_item in cart_items:
            cart_item.subtotal = cart_item.product.price * cart_item.quantity
            total += cart_item.subtotal
            quantity += cart_item.quantity
            total_cost = total + 40
        
    except ObjectDoesNotExist:
        pass
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'total_cost' : total_cost,
    }
    return render(request, 'cart.html', context)

@login_required(login_url='signin')
def remove_cart_item(request, product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

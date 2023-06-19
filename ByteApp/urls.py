from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fashion_child_product/', views.fashion_child_product, name='fashion-child-product'),
    path('laptop_product/', views.laptop_product, name='laptop-product'),
    path('footwear_product/', views.footwear_product, name='footwear-product'),
    path('footwear_product/', views.footwear_product, name='footwear-product'),
    path('gift_product/', views.gift_product, name='gift-product'),
    path('phone_product/', views.phone_product, name='phone-product'),
    path('toys_product/', views.toys_product, name='toys-product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('contact_issue', views.contact_issue, name='contact_issue'),
    path('account/', views.account, name='account'),
    #path('product_details_child/<slug:cat_slug>/<slug:product_slug>/', views.product_detials_child, name='product_detials_child'),
    
    path('product_details_child/<slug:cat_slug>/<slug:product_slug>/', views.product_detials_child, name='product_detials_child'),
    #path('product_details_child/<slug:cat_slug>/', views.product_detials_child, name='product_detials_child'),
    
    path('product_detials_gift/<slug:cat_slug>/<slug:product_slug>/', views.product_detials_gift, name='product_detials_gift'),
    path('product_detials_phone/<slug:cat_slug>/<slug:product_slug>/', views.product_detials_phone, name='product_detials_phone'),
    path('product_detials_footwear/<slug:cat_slug>/<slug:product_slug>/', views.product_detials_footwear, name='product_detials_footwear'),
    path('product_detials_toy/<slug:cat_slug>/<slug:product_slug>/', views.product_detials_toy, name='product_detials_toy'),
    path('product_detials_laptop/<slug:cat_slug>/<slug:product_slug>', views.product_detials_laptop, name='product_detials_laptop'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
]

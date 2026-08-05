from django.contrib import admin
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #urls of product
    path('product',allproducts,name='products'),
    path('prodet/<int:pid>',productdetailpage,name='product_details'),
    path('allcat',allcategory,name='category'),
    path("catpro/<int:cid>",categoryproducts,name="cat_products"),
    path("addpro",addproduct),
    path("editpro/<int:pid>",editproduct,name="edit_product"),
    path("deletepro/<int:pid>",deleteproduct,name="delete_product"),

    #urls of user
    path("login",loginpage,name="login"),
    path("logout",logoutpage,name="logout"),
    path("register",registerpage,name="register"),
    path("profiles",profilepage,name="profiles"),
    
    #urls of cart
    path("addtocart/<int:pid>", add_to_cart, name="add_to_cart"),
    path("cart/", view_cart, name="view_cart"),
    path("updatecart/<int:id>/", update_cart, name="update_cart"),
    path("removecart/<int:id>", remove_from_cart, name="remove_from_cart")
]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

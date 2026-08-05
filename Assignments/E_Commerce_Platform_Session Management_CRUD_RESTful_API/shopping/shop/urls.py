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
    path("removecart/<int:id>", remove_from_cart, name="remove_from_cart"),

    #urls of order
    path("placeorder/",place_order, name="place_order"),
    path("orders/",my_orders, name="my_orders"),
    path("orders/<int:order_id>/",order_details,name="order_details"),
    path("cancelorder/<int:order_id>/",cancel_order,name="cancel_order"),

    #urls for product API
    path("api/products/",product_api, name="product_api"),
    path("api/products/<int:pid>/",single_product_api,name="single_product_api"),
    path("api/addproduct/",add_product_api,name="add_product_api"),
    path("api/updateproduct/<int:pid>/",update_product_api,name="update_product_api"),
    path("api/deleteproduct/<int:pid>/",delete_product_api,name="delete_product_api"),

    #urls for order API
    path("api/orders/",order_api, name="order_api"),
    path("api/orders/<int:oid>/",single_order_api,name="single_order_api"),
    path("api/addorder/",add_order_api,name="add_order_api"),
    path("api/updateorder/<int:oid>/",update_order_api,name="update_order_api"),
    path("api/deleteorder/<int:oid>/",delete_order_api,name="delete_order_api"),
]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

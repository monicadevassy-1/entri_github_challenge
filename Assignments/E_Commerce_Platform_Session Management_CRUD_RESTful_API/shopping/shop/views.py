
from django.shortcuts import render,redirect
from .models import *
from .forms import *
    
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
#------------------------------------------------------------------- related to Products
@login_required(login_url="/shop/login")
def allproducts(request):
    pro = Product.objects.all()
    return render(request, "product.html", {'pro': pro})

def allcategory(request):
    cat = Category.objects.all()
    return render(request, "allcat.html", {'cat': cat})

def productdetailpage(request, pid):
    pro = Product.objects.get(id = pid)
    recent = request.session.get("recent", [])
    if pid in recent:
        recent.remove(pid)
    # Add current product at the beginning
    recent.insert(0, pid)
    # Keep only the latest 5 products
    recent = recent[:5]
    request.session["recent"] = recent
    # Fetch recently viewed products
    recent_products = Product.objects.filter(id__in=recent).exclude(id=pid)
    # Maintain the same order as in the session
    recent_products = sorted(recent_products,key=lambda p: recent.index(p.id))
    return render(request, "details.html", {"pro": pro,"recent_products": recent_products,})

def categoryproducts(request, cid):
    pro = Product.objects.filter(cat = cid)
    return render(request, "catpro.html",{'pro':pro})

def addproduct(request):
    if request.method=="POST":
        form= ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(allproducts)
    else:
        form= ProductForm()
    return render(request,"addpro.html",{"form":form})

def editproduct(request,pid):
    pro_obj=Product.objects.get(id=pid)
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=pro_obj)
        if form.is_valid():
            form.save()
            return redirect(allproducts)
    else:
        form=ProductForm(instance=pro_obj)
    return render(request,"editpro.html",{"form":form})

def deleteproduct(request,pid):
    pobj=Product.objects.get(id=pid)
    if request.method=="POST":
        pobj.delete()
        return redirect(allproducts)
    return render(request,"deletepro.html",{"pro":pobj})


#----------------------------------------------------------------------- related to User
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("products")
    if request.method == "POST":
        username = request.POST.get("usern")
        password = request.POST.get("passw")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("products")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "login.html")
    return render(request, "login.html")


def logoutpage(request):
    logout(request)
    messages.success(request,"***user logged out***")
    return redirect(loginpage)

def registerpage(request):
    if request.method=="POST":
        form=RegForm(request.POST)
        if form.is_valid():   
            user = form.save()
            
            cart = Cart()
            cart.user = user
            cart.save()

            profile = Profile()
            profile.user = user
            profile.email = user.email
            profile.save()

            messages.success(request,"user registered successfully!!!!!!!")
            return redirect(loginpage)
    else:
        form=RegForm()
    return render(request,"register.html",{'form':form})



@login_required(login_url="/shop/login")
def profilepage(request):
    pro = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=pro)
        if form.is_valid():
            form.save()
            return redirect("profiles")
    else:
        form = ProfileForm(instance=pro)
    return render(request, "profiles.html", {"form": form})


#-------------------------------------------------------------------view related to Cart and  Cartitems

@login_required(login_url="/shop/login")
def add_to_cart(request, pid):
    product = Product.objects.get(id=pid)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(cart=cart,product=product, quantity=1)
    cart_item.save()
    # Store total number of items in session
    total = 0
    for item in CartItem.objects.filter(cart=cart):
        total += item.quantity
    request.session["cart_count"] = total
    messages.success(request, "Product added to cart successfully.")
    return redirect(allproducts)

@login_required(login_url="/shop/login")
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = 0
    for item in cart_items:
        total += item.sub_total()
    return render(request, "cart.html", {"cart_items": cart_items,"total": total,})


@login_required(login_url="/shop/login")
def update_cart(request, item_id):
    item = CartItem.objects.get(id=item_id)
    if request.method == "POST":
        qty = int(request.POST.get("qty"))
        if qty < 1:
            qty = 1
        item.quantity = qty
        item.save()
        total = 0
        cart_items = CartItem.objects.filter(cart=item.cart)
        for i in cart_items:
            total += i.quantity
        request.session["cart_count"] = total
        messages.success(request, "Cart updated successfully.")
        return redirect("view_cart")
    return render(request, "update.html", {"item": item})

@login_required(login_url="/shop/login")
def remove_from_cart(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart = cart_item.cart
    cart_item.delete()
    total = 0
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        total += item.quantity
    request.session["cart_count"] = total
    messages.success(request, "Product removed from cart.")
    return redirect("view_cart")


#-------------------------------------------------------------------view related to Order and  Orderitems
@login_required(login_url="/shop/login")
def place_order(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect("view_cart")
    total = 0
    for item in cart_items:
        total += item.sub_total()
    order = Order()
    order.user = request.user
    order.total = total
    order.save()
    for item in cart_items:
        order_item = OrderItem()
        order_item.order = order
        order_item.product = item.product
        order_item.quantity = item.quantity
        order_item.price = item.product.price
        order_item.save()
    cart_items.delete()
    request.session["cart_count"] = 0
    messages.success(request, "Order placed successfully.")
    return redirect("my_orders")

@login_required(login_url="/shop/login")
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-order_date")
    return render(request, "orders.html", {"orders": orders})

@login_required(login_url="/shop/login")
def order_details(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, "order_details.html", {"order": order, "order_items": order_items,})


@login_required(login_url="/shop/login")
def cancel_order(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    if order.status == "Pending":
        order.status = "Cancelled"
        order.save()
        messages.success(request, "Order cancelled successfully.")
    return redirect("my_orders")


#-------------------------------------------------------------------view related to product API
@api_view(["GET"])
def product_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def single_product_api(request, pid):
    product = Product.objects.get(id=pid)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(["POST"])
def add_product_api(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["PUT"])
def update_product_api(request, pid):
    product = Product.objects.get(id=pid)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
def delete_product_api(request, pid):
    product = Product.objects.get(id=pid)
    product.delete()
    return Response({"message": "Product deleted successfully"})

#--------------------------------------------------------------------view related to order API
@api_view(["GET"])
def order_api(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def single_order_api(request, oid):
    order = Order.objects.get(id=oid)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(["POST"])
def add_order_api(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["PUT"])
def update_order_api(request, oid):
    order = Order.objects.get(id=oid)
    serializer = OrderSerializer(order,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
def delete_order_api(request, oid):
    order = Order.objects.get(id=oid)
    order.delete()
    return Response({"message": "Order deleted successfully"})

from django.shortcuts import render,redirect
from .models import Product,Category,Cart,CartItem,Profile
from .forms import ProductForm,RegForm,ProfileForm
    
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    return render(request, "details.html",{'pro':pro})

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

    cart_item = CartItem()
    cart_item.cart = cart
    cart_item.product = product
    cart_item.quantity = 1
    cart_item.save()
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
def update_cart(request, id):
    item = CartItem.objects.get(id=id)
    if request.method == "POST":
        qty = request.POST.get("qty")
        item.quantity = qty
        item.save()
        messages.success(request, "Cart updated successfully.")
        return redirect("view_cart")
    return render(request, "update.html", {"item": item})


@login_required(login_url="/shop/login")
def remove_from_cart(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    messages.success(request, "Product removed from cart.")
    return redirect("view_cart")
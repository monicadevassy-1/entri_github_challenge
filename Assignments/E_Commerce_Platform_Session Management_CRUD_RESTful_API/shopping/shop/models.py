from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    des=models.TextField(blank=True)
    cimg=models.ImageField(upload_to="category",blank=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    des=models.TextField(blank=True)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    pimg=models.ImageField(upload_to="product",blank=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
   
    def sub_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    email=models.EmailField()
    phone = models.CharField(max_length=15,blank=True)
    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product.name
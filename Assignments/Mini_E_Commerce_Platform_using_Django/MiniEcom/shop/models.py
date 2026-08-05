from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,blank=True)
    address=models.TextField(blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES=(('pending','Pending'),
                   ('accepted','Accepted'),
                   ('rejected','Rejected'))
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    def __str__(self):
        return self.customer.name
    
class OrderItem(models.Model):
    orderitem_id = models.AutoField(primary_key=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f"{self.product.name} {self.quantity}"
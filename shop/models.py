from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=4)
    # description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def _str_(self):
        return str(self.id)+' '+str(self.name)

    

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image=models.ForeignKey(Product,on_delete=models.PROTECT)

    def _str_(self):
        return f"{self.product.product_name} x {self.quantity}"

# Create your models here.

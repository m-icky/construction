from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)

class user_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    
class shop_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    
class add_product(models.Model):
    shop=models.ForeignKey(shop_reg, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='images/', null=True)
    quantity = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(add_product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0,null=True)
    total = models.CharField(max_length=100,null=True)
    payment = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    delivery = models.CharField(max_length=100,null=True)
    shop=models.ForeignKey(shop_reg, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=50,null=True)


    
    
class feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(add_product, on_delete=models.CASCADE, null=True)
    shop=models.ForeignKey(shop_reg, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=50,null=True)
    feedback = models.CharField(max_length=50,null=True)
    action = models.CharField(max_length=50,null=True)
    actions = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    statuss = models.CharField(max_length=50,null=True)





    



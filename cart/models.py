from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username
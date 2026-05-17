from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    price = models.FloatField()
    discount_percentage = models.FloatField()

    rating = models.FloatField()
    stock = models.IntegerField()

    thumbnail = models.URLField()

    sku = models.CharField(max_length=100)

    warranty_information = models.CharField(max_length=255)
    shipping_information = models.CharField(max_length=255)

    availability_status = models.CharField(max_length=100)

    return_policy = models.CharField(max_length=255)

    minimum_order_quantity = models.IntegerField()

    def __str__(self):
        return self.title
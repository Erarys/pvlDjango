from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ["name", "price"]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="goods")
    image = models.ImageField(upload_to='image', default='default.jpg')
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f"Коффе {self.name!r} стоит {self.price}тг"


class Order(models.Model):
    name = models.CharField(max_length=100, blank=False, default="None")
    email = models.CharField(max_length=100, blank=False, default="None")
    coffee = models.ManyToManyField(Product, related_name="orders")
    count = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

from django.db import models


# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100, unique=True)
    item_desc = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=1000, default="https://cdn-icons-png.flaticon.com/512/1147/1147805.png")


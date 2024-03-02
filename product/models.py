from django.db import models
from categories.models import *

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=40,unique=True)
    model = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    type = models.CharField(null=True)
    image = models.ImageField(upload_to='product/images',blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




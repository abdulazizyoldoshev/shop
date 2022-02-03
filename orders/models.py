from django.db import models
from users.models import UserModel
from products.models import ProductModel


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, blank=True, null=True)
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

# Create your models here.

from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
# MaxValueValidator, MinValueValidator
from configuration.validators import PhoneValidator


class ProductModel(models.Model):
    number = models.CharField(max_length=12, validators=[PhoneValidator])
    email = models.EmailField(validators=[EmailValidator()], null=True, blank=True)
    username = models.CharField(max_length=50, validators=[MinLengthValidator(8), MaxLengthValidator(50)])

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class CategoryModel(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

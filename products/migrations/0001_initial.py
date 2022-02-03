# Generated by Django 4.0.1 on 2022-01-10 15:12

import configuration.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(30), django.core.validators.EmailValidator()])),
                ('number', models.CharField(max_length=12, validators=[configuration.validators.PhoneValidator()])),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(1)])),
                ('count', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('img', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('description', models.TextField(validators=[configuration.validators.MyValidators()])),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]

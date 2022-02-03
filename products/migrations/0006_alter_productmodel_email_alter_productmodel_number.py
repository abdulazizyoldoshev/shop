# Generated by Django 4.0.1 on 2022-01-31 12:14

import configuration.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='number',
            field=models.CharField(max_length=12, validators=[configuration.validators.PhoneValidator]),
        ),
    ]

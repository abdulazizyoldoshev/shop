# Generated by Django 4.0.1 on 2022-01-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='card',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='zip_code',
            field=models.PositiveIntegerField(),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-28 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermodel_card_alter_usermodel_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='zip_code',
        ),
    ]

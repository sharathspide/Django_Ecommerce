# Generated by Django 5.0.1 on 2024-03-16 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Women_Ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Sellers',
            new_name='Seller',
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-11 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_product_is_sale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_sale',
            new_name='On_Sale',
        ),
    ]

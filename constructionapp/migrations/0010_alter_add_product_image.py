# Generated by Django 4.1.1 on 2022-09-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0009_remove_add_product_address_remove_add_product_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_product',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

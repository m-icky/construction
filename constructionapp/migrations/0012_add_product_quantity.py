# Generated by Django 4.1.1 on 2022-10-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0011_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_product',
            name='quantity',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0030_remove_cart_action_remove_cart_adminrply_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='feedback',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
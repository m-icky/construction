# Generated by Django 4.1.1 on 2022-09-28 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('constructionapp', '0008_shop_reg_add_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_product',
            name='address',
        ),
        migrations.RemoveField(
            model_name='add_product',
            name='phone',
        ),
        migrations.AddField(
            model_name='add_product',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='add_product',
            name='image',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='add_product',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='add_product',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='add_product',
            name='price',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

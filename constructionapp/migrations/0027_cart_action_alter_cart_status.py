# Generated by Django 4.1.1 on 2022-11-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0026_feedback_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='action',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
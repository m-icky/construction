# Generated by Django 4.1.1 on 2022-10-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0023_feedback_status_delete_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='actions',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 3.1 on 2020-08-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

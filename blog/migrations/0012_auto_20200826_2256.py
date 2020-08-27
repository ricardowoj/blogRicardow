# Generated by Django 3.1 on 2020-08-27 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='facebook',
            new_name='facebook_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

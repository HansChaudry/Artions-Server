# Generated by Django 5.0 on 2024-01-06 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='following_id',
            new_name='followee_id',
        ),
    ]

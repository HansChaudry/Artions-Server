# Generated by Django 5.0 on 2024-01-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.IntegerField(blank=True, default=0, verbose_name='followers'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.IntegerField(blank=True, default=0, verbose_name='followers'),
        ),
    ]

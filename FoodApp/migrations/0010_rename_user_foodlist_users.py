# Generated by Django 4.0.6 on 2022-07-14 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0009_foodlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodlist',
            old_name='user',
            new_name='users',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-14 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_food_delete_foodcals'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Food',
        ),
    ]
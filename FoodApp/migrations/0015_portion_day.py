# Generated by Django 4.0.6 on 2022-07-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0014_portion_meals'),
    ]

    operations = [
        migrations.AddField(
            model_name='portion',
            name='day',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
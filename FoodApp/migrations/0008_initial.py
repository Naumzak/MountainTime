# Generated by Django 4.0.6 on 2022-07-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FoodApp', '0007_delete_foodcals'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodcategory', models.CharField(blank=True, db_column='FoodCategory', max_length=100, null=True)),
                ('fooditem', models.CharField(blank=True, db_column='FoodItem', max_length=100, null=True)),
                ('per100grams', models.CharField(blank=True, max_length=10, null=True)),
                ('cals_per100grams', models.CharField(blank=True, db_column='Cals_per100grams', max_length=10, null=True)),
                ('kj_per100grams', models.CharField(blank=True, db_column='KJ_per100grams', max_length=10, null=True)),
            ],
            options={
                'db_table': 'food_cals',
            },
        ),
    ]
from django.db import models
from django.contrib.auth.models import User


class FoodCals(models.Model):
    foodcategory = models.CharField(db_column='FoodCategory', blank=True, null=True,
                                    max_length=100)  # Field name made lowercase.
    fooditem = models.CharField(db_column='FoodItem', blank=True, null=True,
                                max_length=100)  # Field name made lowercase.
    per100grams = models.CharField(blank=True, null=True, max_length=10)
    cals_per100grams = models.CharField(db_column='Cals_per100grams', blank=True,
                                        null=True, max_length=10)  # Field name made lowercase.
    kj_per100grams = models.CharField(db_column='KJ_per100grams', blank=True, null=True,
                                      max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'food_cals'

    def __str__(self):
        return self.fooditem


class Portion(models.Model):
    class Meals(models.IntegerChoices):
        BREAKFAST = 1
        LUNCH = 2
        DINNER = 3
        SNACK = 4

    food = models.ForeignKey(FoodCals, on_delete=models.SET_NULL, null=True)
    weight = models.SmallIntegerField()
    cals = models.SmallIntegerField()
    meals = models.IntegerField(choices=Meals.choices, default=Meals.BREAKFAST)
    day = models.SmallIntegerField()
    def __str__(self):
        return f'{self.food} - {self.weight}'


class FoodList(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    food = models.ManyToManyField(Portion, null=True, blank=True)
    days = models.SmallIntegerField( default=1)

    class Meta:
        ordering = ('name',)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

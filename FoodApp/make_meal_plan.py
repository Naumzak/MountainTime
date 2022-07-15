from FoodApp.models import FoodCals, FoodList, Portion
from django.core import serializers


class MealPlan:
    def __init__(self, food_list_id):
        self.ready_food_list = FoodList.objects.get(pk=food_list_id)

    def make_plan(self):
        meals = ['Breakfast', 'Lunch', 'Dinner', 'Snack']
        ready_plan = {}
        for day in range(1, self.ready_food_list.days + 1):
            one_day = {}
            for meal in range(1, 5):
                one_meal = self.ready_food_list.food.filter(meals=meal, day=day)[::1]
                cals_in_one_meal = sum([i.cals for i in one_meal])
                grams_in_one_meal = sum([i.weight for i in one_meal])
                one_day[meals[meal - 1]] = [one_meal, cals_in_one_meal, grams_in_one_meal]
            ready_plan[day] = one_day
        return ready_plan


class AddFoodToPlan:
    def __init__(self, request):
        self.meals = {'Breakfast': 1, 'Lunch': 2, 'Dinner': 3, 'Snack': 4}
        self.weight = request.POST['weight']
        self.food = FoodCals.objects.get(pk=request.POST['item'])
        self.calculator_id = request.GET['calculator']

        meal_and_day = request.POST['meal'].split('-')
        self.meal = self.meals[meal_and_day[0]]
        self.day = meal_and_day[1]

    def count_calories(self):
        self.cals = int(int(self.food.cals_per100grams) / 100 * int(self.weight))
        return self.cals

    def create_portion(self):
        p = Portion(food=self.food, weight=self.weight, meals=self.meal, day=self.day, cals=self.count_calories())
        p.save()
        return p

    def save_portion_to_food_list(self):
        FoodList.objects.get(pk=self.calculator_id).food.add(self.create_portion())


class DeleteFoodFromPlan:
    def __init__(self, request):
        self.portion_id = request.POST['delete']

    def delete_portion(self):
        portion = Portion.objects.get(pk=self.portion_id)
        Portion.delete(portion)

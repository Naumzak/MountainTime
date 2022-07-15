import json

from django.shortcuts import render, redirect
from django.views import View
from FoodApp.make_meal_plan import MealPlan, AddFoodToPlan, DeleteFoodFromPlan
from FoodApp.models import FoodCals, FoodList, Portion


class EditCalculator(View):
    def get(self, request):
        food_list_id = request.GET['calculator']
        ready_food_list = MealPlan(food_list_id).make_plan()
        food_list = FoodCals.objects.all()
        return render(request, 'calculator.html', context={'food_list': food_list, 'ready_food_list': ready_food_list,
                                                           'food_list_id': food_list_id})


# Create your views here.

class AddItemCalculator(View):
    def post(self, request):
        AddFoodToPlan(request).save_portion_to_food_list()
        calculator_id = request.GET['calculator']
        response = redirect('update_calculator')
        response['Location'] += f'?calculator={calculator_id}'
        return response


class DeleteItemCalculator(View):
    def post(self, request):
        DeleteFoodFromPlan(request).delete_portion()
        calculator_id = request.GET['calculator']
        response = redirect('update_calculator')
        response['Location'] += f'?calculator={calculator_id}'
        return response


class AddDayCalculator(View):
    def post(self, request):
        calculator_id = request.GET['calculator']
        food_list = FoodList.objects.filter(pk=calculator_id)
        days= FoodList.objects.get(pk=calculator_id).days
        food_list.update(days=days+1)
        response = redirect('update_calculator')
        response['Location'] += f'?calculator={calculator_id}'
        return response


class DeleteDayCalculator(View):
    def post(self, request):
        calculator_id = request.GET['calculator']
        food_list = FoodList.objects.filter(pk=calculator_id)
        days= FoodList.objects.get(pk=calculator_id).days
        food_list.update(days=days-1)
        response = redirect('update_calculator')
        response['Location'] += f'?calculator={calculator_id}'
        return response


class ListCalculators(View):
    def get(self, request):
        calculator_lists = FoodList.objects.filter(users=request.user)
        return render(request, 'calculator_list.html', context={'calculator_lists': calculator_lists})


class CreateCalculatorView(View):
    def get(self, request):
        name = request.GET['name']
        c = FoodList(name=name)
        c.save()
        c.users.add(request.user)
        return redirect('calculators_list')

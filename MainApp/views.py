from django.shortcuts import render, redirect
from django.views import View


class MainMenu(View):
    def get(self, request):
        return render(request, 'main_menu.html')

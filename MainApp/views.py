from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class MainMenu(View):
    def get(self, request):
        return render(request, 'main_menu.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(f'{username} logged')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return HttpResponse(f'{username} created')
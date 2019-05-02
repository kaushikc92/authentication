from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import requests

def create_account(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        data = { 
            'username': request.POST['username'],
            'email': request.POST['email'],
            'firstname': request.POST['firstname'],
            'lastname': request.POST['lastname']
        }
        requests.post(url='http://cdrive/register-user/', data=data)
        #requests.post(url='http://0.0.0.0:8001/register-user/', data=data)
        return redirect('/accounts/login/')
    elif request.method == 'GET':
        return render(request, 'registration/create-user.html')

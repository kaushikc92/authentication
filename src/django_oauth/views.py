from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from oauth2_provider.models import Application
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
        
        if settings.DEBUG_LOCAL:
            requests.post(url='http://0.0.0.0:8001/api/v1/cdrive/register-user/', data=data)
        else:
            requests.post(url='http://cdrive/api/v1/cdrive/register-user/', data=data)

        cdrive_url = Application.objects.filter(name='CDrive')[0].redirect_uris
        return redirect(cdrive_url)

    elif request.method == 'GET':
        return render(request, 'registration/create-user.html')

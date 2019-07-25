from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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
            requests.post(url='http://0.0.0.0:8001/register-user/', data=data)
        else:
            requests.post(url='http://cdrive/register-user/', data=data)

        cdrive_url = Application.objects.filter(name='CDrive')[0].redirect_uris
        return redirect(cdrive_url)

    elif request.method == 'GET':
        return render(request, 'registration/create-user.html')

@method_decorator(csrf_exempt)
def register_application(request):
    if request.method == 'POST':
        app_name = request.POST['app_name']
        redirect_url = request.POST['redirect_url']
        app = None
        if Application.objects.filter(name=app_name).exists():
            app = Application.objects.filter(name=app_name)[0]
            app.redirect_uris = app.redirect_uris + " " + redirect_url
        else:
            admin_user = User.objects.all()[0]
            app = Application(
                name = app_name,
                user = admin_user,
                redirect_uris = redirect_url,
                client_type = "public",
                authorization_grant_type = "Authorization code",
            )
            
        app.save()
        return JsonResponse({'clientId': app.client_id, 'clientSecret': app.client_secret}, status=201)

    else:
        return HttpResponse(status=200)

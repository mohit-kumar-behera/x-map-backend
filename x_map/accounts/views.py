from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model, authenticate, login

from accounts.utils import create_response_obj
User = get_user_model()
import json

def home(request):
  print(dir(request))
  user = request.user
  return HttpResponse(f'Hello {user}')


@csrf_exempt
def login_api_handler(request):
  if request.method == 'POST':
    req_data = json.loads(request.body.decode('utf-8'))
    email = req_data.get('email')
    try:
      User.objects.get(email=email)
    except User.DoesNotExist:
      response_obj, status = create_response_obj(status=404, success='failure', message='Incorrect Email or Password')
    else:
      password = req_data.get('password')
      authenticated_user = authenticate(request, email=email, password=password)
      if authenticated_user is not None:
        response_obj, status = create_response_obj(status=200, success='succes', message='Successfully logged in')
        print(authenticated_user)
        login(request, authenticated_user)
      else:
        response_obj, status = create_response_obj(status=404, success='failure', message='Incorrect Email or Password')
    return HttpResponse(json.dumps(response_obj), status=status)


@csrf_exempt
def register_api_handler(request):
  if request.method == 'POST':
    req_data = json.loads(request.body.decode('utf-8'))
    email = req_data.get('email')
    try:
      User.objects.get(email=email)
    except User.DoesNotExist:
      # continue with user creation
      password = req_data.get('password')
      user = User.objects.create_user(email=email, password=password)
      user.save()
      response_obj, status = create_response_obj(status=201, success='success', message='User created successfully')
    else:
      # User with this email already exists
      response_obj, status = create_response_obj(status=400, success='failure', message='User with this email id already exists')
    return HttpResponse(json.dumps(response_obj), status=status)
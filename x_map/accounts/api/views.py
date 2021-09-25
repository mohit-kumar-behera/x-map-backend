from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth import get_user_model, authenticate
from django.views.decorators.csrf import csrf_exempt

from accounts.api.utils import create_200_response, create_400_response, create_404_response
from accounts.api.serializers import UserSerializer
User = get_user_model()

import json

@csrf_exempt
def login_api_handler(request):
  if request.method == 'POST':
    req_data = json.loads(request.body.decode('utf-8'))
    email = req_data.get('email')
    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      response_obj = create_404_response()
      return HttpResponse(json.dumps(response_obj), status=404)
    else:
      password = req_data.get('password')
      authenticated_user = authenticate(request, email=email, password=password)
      if authenticated_user is not None:
        response_obj = create_200_response('Successfully logged in')
        return HttpResponse(json.dumps(response_obj), status=200)
      else:
        response_obj = create_404_response()
        return HttpResponse(json.dumps(response_obj), status=404)


@csrf_exempt
@api_view(['POST'])
def register_api_handler(request):
  if request.method == 'POST':
    req_data = request.data
    email = req_data.get('email')
    try:
      User.objects.get(email=email)
    except User.DoesNotExist:
      password = req_data.get('password')
      user = User.objects.create_user(email=email, password=password)
      user.save()
      serializer = UserSerializer(user, many=False)
      response_obj = create_200_response(serializer.data)
      return Response(response_obj, status=status.HTTP_200_OK)
    else:
      response_obj = create_400_response()
      return Response(response_obj, status=status.HTTP_400_BAD_REQUEST)
      
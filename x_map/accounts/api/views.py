from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from accounts.api.utils import create_200_response, create_400_response, create_404_response
from accounts.api.serializers import UserSerializer
User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_login_api_handler(request):
  try:
    user = User.objects.get(email=request.user)
  except:
    response_obj = create_404_response()
    return Response(response_obj, status=status.HTTP_404_NOT_FOUND)
  else:
    serializer = UserSerializer(user, many=False)
    response_obj = create_200_response(serializer.data)
    return Response(response_obj, status=status.HTTP_200_OK)


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
      
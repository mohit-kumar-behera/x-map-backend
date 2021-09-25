from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import HttpResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check(request):
  print(request.user)
  return Response('hey man', status=status.HTTP_200_OK)
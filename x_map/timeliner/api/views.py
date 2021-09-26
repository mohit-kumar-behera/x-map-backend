from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from timeliner.models import Location, Timeliner
from timeliner.api.serializers import TimeLinerSerializer

from accounts.api.utils import create_200_response, create_404_response

User = get_user_model()

@api_view(['GET'])
def fetch_all_timeline_handler(request):
  if request.method == 'GET':
    timelines = Timeliner.objects.all()
    serializer = TimeLinerSerializer(timelines, many=True)
    response_obj = create_200_response(serializer.data)
    return Response(response_obj, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def fetch_user_timeline_handler(request):
  try:
    user = request.user
  except:
    response_obj = create_404_response()
    return Response(response_obj, status=status.status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    try:
      timeline = Timeliner.objects.filter(user=user)
    except:
      response_obj = create_404_response()
      return Response(response_obj, status=status.status.HTTP_404_NOT_FOUND)
    else:
      serializer = TimeLinerSerializer(timeline, many=True)
      response_obj = create_200_response(serializer.data)
      return Response(response_obj, status=status.HTTP_200_OK)
  if request.method == 'POST':
    title = request.data.get('title')
    description = request.data.get('experience')
    location = request.data.get('location')
    display_name = location.get('display_name')
    longitude = location.get('longitude')
    latitude = location.get('latitude') 

    timeline = Timeliner.objects.create(user=user, name=title, description=description)
    timeline.save()

    location = Location.objects.create(timeliner=timeline, latitude=latitude, longitude=longitude, display_name=display_name)
    location.save()

    response_obj = create_200_response("i reached here")
    return Response(response_obj, status=status.HTTP_200_OK)


"""
{'location': {'display_name': 'Paradeep, Paradip, Jagatsinghapur, Odisha, India', 'latitude': '20.2685001', 'longitude': '86.65105802462674'}, 
'image': {}, 
'title': 'Baby Will Travel - This name can be used as an example for youngsters who actually want to travel.', 'experience': 'Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown', 'my_image': {}}

"""


@api_view(['GET'])
def fetch_user_timeline_post_handler(request, pid):
  if request.method == 'GET':
    try:
      timeline = Timeliner.objects.get(id=pid)
    except Timeliner.DoesNotExist:
      response_obj = create_404_response()
      return Response(response_obj, status=status.status.HTTP_404_NOT_FOUND)
    else:
      serializer = TimeLinerSerializer(timeline, many=False)
      response_obj = create_200_response(serializer.data)
      return Response(response_obj, status=status.HTTP_200_OK)


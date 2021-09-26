from rest_framework import serializers
from timeliner.models import Timeliner, Location

from accounts.api.serializers import UserSerializer


class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    exclude = ('timeliner',)



class TimeLinerSerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False)
  location = serializers.SerializerMethodField()
  
  class Meta:
    model = Timeliner
    fields = '__all__'

  def get_location(self, timeline):
    location = timeline.location
    serializer = LocationSerializer(location, many=False)
    return serializer.data
  
from django.db import models
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()

def image_directory_path(instance, filename):
  extension = filename.split('.')[1]
  file_name = instance.name[:30]
  filename = f'images/{instance.user.username}/{file_name}.{extension}'
  return filename

class Timeliner(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField()
  image_one = models.ImageField(upload_to=image_directory_path, blank=True, null=True)
  image_two = models.ImageField(upload_to=image_directory_path, blank=True, null=True)

  def __str__(self):
    return self.name


class Location(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  timeliner = models.OneToOneField(Timeliner, on_delete=models.CASCADE)
  latitude = models.CharField(max_length=25, null=True, blank=True)
  longitude = models.CharField(max_length=25, null=True, blank=True)
  display_name = models.TextField(null=True, blank=True)
  mapurl = models.URLField(null=True, blank=True)

  def __str__(self):
    return f'{self.display_name}'

  def save(self, *args, **kwargs):
    self.mapurl = f'https://www.google.com/maps/dir//{self.latitude},{self.longitude}'
    super(Location, self).save(*args, **kwargs)

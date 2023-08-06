from django.db import models
from django.contrib.gis.db import models as gis_models


class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    coordinates = gis_models.PointField()

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class TrackData(models.Model):
    idTracker = models.IntegerField()
    dataInfo = models.TextField()
    radius = models.IntegerField()
    is_done = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    dateReached = models.TextField()
    
    class Meta:
        ordering = ['idTracker']
from django.db import models

# Create your models here.
class short(models.Model):
    video_title = models.CharField(max_length=200)
    video_url = models.CharField(max_length=1000)
    video_img = models.CharField(max_length=1000)
    video_dur = models.CharField(max_length=10)
    categroty = models.CharField(max_length=10)
    def __str__(self):
        return self.video_title
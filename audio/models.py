from django.db import models
from django.db.models.base import Model

from completedCourses.models import Category
# Create your models here.

audioCat = (
 ('عام','عام'),
('جذور-قرآنية','جذور-قرآنية'),
('ماذا-أتعلم-وكيف-أتعلم','ماذا-أتعلم-وكيف-أتعلم'),
('تأسيس-وعي-مسلم-معاصر-2','تأسيس-وعي-مسلم-معاصر-2'),
('الدورة-التعريفية-بالعلوم-الإسلامية','الدورة-التعريفية-بالعلوم-الإسلامية'),
('برنامج-برة-الصندوق','برنامج-برة-الصندوق'),
('مدخل-إلى-العلوم-الإنسانية','مدخل-إلى-العلوم-الإنسانية'),
)
class audio (models.Model):
    audio_src = models.CharField(max_length=850)
    audio_title = models.CharField(max_length=250)
    audio_length = models.CharField(max_length=10)
    audioShareLink = models.CharField(max_length=500)
    audioDownloadLink = models.CharField(max_length=500)
    categroty = models.CharField(max_length=250,default='',choices=audioCat)


    def __str__(self):
        return self.audio_title 

class audioCourse (models.Model):
    Course_title = models.CharField(max_length=255,default='')
    categroty = models.CharField(max_length=250,default='',choices=audioCat)


    def __str__ (self):
        return self.Course_title
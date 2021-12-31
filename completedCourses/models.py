from django.db import models
from django.db.models.deletion import CASCADE
course_cat = (
('تأسيس-وعي-مسلم-معاصر','تأسيس-وعي-مسلم-معاصر'),
('السيرة-النبوية-العهد-المكي','السيرة-النبوية-العهد-المكي'),
('بيت-المسلم','بيت-المسلم'),
('تاريخ-الخلفاء-الراشدين','تاريخ-الخلفاء-الراشدين'),
('مدخل-للتاريخ-الاسلامي','مدخل-للتاريخ-الاسلامي'),
('شيخ-العمود-مدخل-إلي-علم-اللغة','شيخ-العمود-مدخل-إلي-علم-اللغة'),
('علم-النفس','علم-النفس'),
('الوعي-اللغوي','الوعي-اللغوي'),
('تاريخ-الأمويين-والعباسيين','تاريخ-الأمويين-والعباسيين'),
)

# Create your models here.
class course (models.Model):
    course_title = models.CharField(max_length=200)
    course_length = models.CharField(max_length=50)
    course_count = models.IntegerField()
    course_desc = models.CharField(max_length=300)
    categroty = models.CharField(max_length=250,default='',choices=course_cat)


    def __str__(self):
        return self.course_title

class Category(models.Model):
    name = models.CharField(max_length=255,default='')

    def __str__ (self):
        return self.name



class video_list (models.Model):
    video_name = models.CharField(max_length=250,default='')
    video_length = models.CharField(max_length=250,default='')
    categroty = models.CharField(max_length=250,default='',choices=course_cat)
    vido_url = models.CharField(max_length=400,default='')
    def __str__(self):
        return self.video_name 

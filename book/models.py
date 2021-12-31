from django.db import models
class books (models.Model):
    book_title= models.CharField(max_length=250)
    book_url = models.CharField(max_length=600)



    def __str__(self):
        return self.book_title 
# Create your models here.

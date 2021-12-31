from django.shortcuts import render
from . models import books

# Create your views here.
def book(request):
 book=books.objects.filter
 #audios=audio.objects.filter(categroty="عام")
 context = {'books':book}
 return render(request, 'books/books_page.html',context)
 
def home(request):
  return render(request,'completedCourses/index.html') 


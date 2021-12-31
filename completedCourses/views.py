from django.shortcuts import render
from django.core.paginator import Paginator
from . models import Category, course,video_list
from django.shortcuts import get_object_or_404
# Create your views here.
def completed_courses(request):
    completed_courses=course.objects.all()
    context = {'completedcourses':completed_courses}
    return render(request,'completedCourses/courses_page.html',context)
def videolist(request):
    videolist=video_list.objects.all()
    context = {'videoslist':videolist}
    return render(request,'completedCourses/videos_list1.html',context)
def categoryView(request,cats,id=None):
        category_View = video_list.objects.filter(categroty=cats)
        return render(request,'completedCourses/videos_list1.html',{'cats':cats,'category_View':category_View})
def home(request):
       return render(request,'completedCourses/index.html') 
def videoView(request, id,cats):
    videoView = video_list.objects.all()
    video_View = video_list.objects.filter(id=id)
    video_View1 = video_list.objects.filter(id=id+1)
    course_View = video_list.objects.filter(categroty=cats)
    p = Paginator(video_list.objects.filter(categroty=cats),1) # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = p.get_page(page)  
    return render(request,'completedCourses/player.html',{'contacts':contacts,'id':id,'video_View':video_View,'course_View':course_View,'video_View1':video_View1})           


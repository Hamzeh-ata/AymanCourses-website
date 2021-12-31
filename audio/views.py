from django.shortcuts import render
from . models import audio,audioCourse
# Create your views here.
def audios(request,id=0,cat=""):
 audios=audio.objects.all()
 #audios=audio.objects.filter(categroty="عام")
 player = audio.objects.filter(id=id)
 audiocourses = audioCourse.objects.all()
 return render(request, 'audio/audio-page.html', {'audio': audios, 'player':player,'audioCourse':audiocourses})
 
def home(request):
  return render(request,'completedCourses/index.html') 

def coursesAudio(request, cat,id=0) :
 courses_Audio=audio.objects.filter(categroty=cat)
 courses_player = audio.objects.filter(id=id)
 return render(request, 'audio/courses-audio.html', {'cat':cat,'courses_Audio':courses_Audio,'courses_player':courses_player})

from django.shortcuts import render
from .models import short
# Create your views here.
def shorts(request):
    shorts = short.objects.all()
    context = {'shorts':shorts}
    return render(request,'shorts/shorts.html',context)
    
def videoView(request,id,cats):
    video_View = short.objects.filter(id=id)
    return render(request,'shorts/player.html',{'id':id,'video_View':video_View})    
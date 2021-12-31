from django.urls import path, include
from django.urls.conf import include

from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='audio'

urlpatterns = [
   path('', views.home,name='home'),
   path('audio/', views.audios,name='audio'),
   path('audio/<str:cat>', views.coursesAudio,name='categorys'),
   path('audio/<int:id>/', views.audios, name='player'),
   path('audio/<str:cat>/<int:id>/', views.coursesAudio,name='coursesAudio'),

]
urlpatterns += static(settings.STATIC_URL,DOCUMENT_ROOT=settings.STATIC_ROOT)
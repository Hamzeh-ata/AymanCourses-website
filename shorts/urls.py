from django.urls import path, include
from django.urls.conf import include

from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='shorts'

urlpatterns = [
    path('shorts/', views.shorts,name='shorts'),
    path('shorts/<str:cats>/<int:id>/', views.videoView, name='videos_shorts'),

]
urlpatterns += static(settings.STATIC_URL,DOCUMENT_ROOT=settings.STATIC_ROOT)
from django.urls import path, include
from django.urls.conf import include

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='books'

urlpatterns = [
   path('', views.home,name='home'),
   path('books/', views.book,name='books'),


]
urlpatterns += static(settings.STATIC_URL,DOCUMENT_ROOT=settings.STATIC_ROOT)
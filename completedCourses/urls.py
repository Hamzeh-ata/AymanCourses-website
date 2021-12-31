from django.urls import path, include
from django.urls.conf import include

from . import views
from . views import categoryView
from django.conf.urls.static import static
from django.conf import settings
app_name='completedCourses'

urlpatterns = [
    path('', views.home,name='home'),
    path('completedcourses/', views.completed_courses,name='completedcourses'),
    path('completedcourses/<str:cats>/', views.categoryView, name='categorys'),
    path('completedcourses/<str:cats>/<int:id>/', views.videoView, name='videos'),
   # path('category/<str:cats>/', categoryView, name='category')
]
urlpatterns += static(settings.STATIC_URL,DOCUMENT_ROOT=settings.STATIC_ROOT)
from django.contrib import admin

# Register your models here.
from . models import course,video_list,Category

admin.site.register(course)
admin.site.register(video_list)
admin.site.register(Category)

admin.site.register
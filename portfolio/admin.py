from django.contrib import admin
from .models import Blog, Project, Photo

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_published']
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_link']
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image_url', 'caption']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo, PhotoAdmin)

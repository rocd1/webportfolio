from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('combined_list/', views.combined_list, name='combined_list'),

    path('add_blog/', views.add_blog, name='add_blog'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blogs/<slug:slug>/edit/', views.update_blog, name='update_blog'),
    path('blogs/<slug:slug>/delete/', views.delete_blog, name='delete_blog'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/new/', views.add_project, name='add_project'),
    path('projects/<int:pk>/edit/', views.update_project, name='update_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),

    path('photos/', views.photo_list, name='photo_list'),
    path('photos/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photos/new/', views.add_photo, name='add_photo'),
    path('photos/<int:pk>/edit/', views.update_photo, name='update_photo'),
    path('photos/<int:pk>/delete/', views.delete_photo, name='delete_photo'),
]

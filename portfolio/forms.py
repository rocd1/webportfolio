from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Blog, Project, Photo



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['slug', 'title', 'content', 'image_url', 'author', 'post_count']

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['slug', 'title', 'content', 'image_url', 'author', 'post_count']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'project_link']

class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'project_link']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image_url', 'caption']

class UpdatePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image_url', 'caption']


class DeleteForm(forms.Form):
    confirm = forms.BooleanField(label='Confirm deletion', required=True)
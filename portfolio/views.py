from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, ProjectForm, PhotoForm
from .models import Blog, Project, Photo

def home(request):
    blogs = Blog.objects.all()
    projects = Project.objects.all()
    photos = Photo.objects.all()
    context = {
        'blogs': blogs,
        'projects': projects,
        'photos': photos
    }
    return render(request, 'portfolio/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('combined_list')
        else:
            return render(request, 'portfolio/user_login.html', {'error': 'Invalid credentials'})
    return render(request, 'portfolio/user_login.html')

def user_logout(request):
    logout(request)
    return redirect('home')


#admin
@login_required(login_url='user_login')
def combined_list(request):
    blogs = Blog.objects.all()
    projects = Project.objects.all()
    photos = Photo.objects.all()
    context = {
        'blogs': blogs,
        'projects': projects,
        'photos': photos
    }
    return render(request, 'portfolio/combined_list.html', context)


#blog
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'portfolio/blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'blog': blog})


@login_required(login_url='user_login')
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        else:
            print(form.errors)  # Debugprintformerrors
    else:
        form = BlogForm()
    return render(request, 'portfolio/add_blog.html', {'form': form})


@login_required(login_url='user_login')
def update_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, 'portfolio/blog_update.html', {'form': form})

@login_required(login_url='user_login')
def delete_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'portfolio/blog_delete.html', {'blog': blog})


#project
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

@login_required(login_url='user_login')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/add_project.html', {'form': form})

@login_required(login_url='user_login')
def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/project_update.html', {'form': form})

@login_required(login_url='user_login')
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'portfolio/project_delete.html', {'project': project})


#photo
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'portfolio/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'portfolio/photo_detail.html', {'photo': photo})

@login_required(login_url='user_login')
def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'portfolio/add_photo.html', {'form': form})

@login_required(login_url='user_login')
def update_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'portfolio/photo_update.html', {'form': form})

@login_required(login_url='user_login')
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('photo_list')
    return render(request, 'portfolio/photo_delete.html', {'photo': photo})

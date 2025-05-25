from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Manga, Chapter

def home(request):
    mangas = Manga.objects.all()
    return render(request, 'blog/home.html', {'mangas': mangas})

def manga_list(request):
    mangas = Manga.objects.all()
    return render(request, 'blog/manga_list.html', {'mangas': mangas})

@login_required(login_url='login')
def detail(request, manga_id):
    manga = get_object_or_404(Manga, pk=manga_id)
    return render(request, 'blog/detail.html', {'manga': manga})

def chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return render(request, 'blog/chapter.html', {'chapter': chapter})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Sửa ở đây
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

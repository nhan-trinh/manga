from django.shortcuts import render, get_object_or_404
from .models import Manga, Chapter

def home(request):
    mangas = Manga.objects.all()
    return render(request, 'blog/home.html', {'mangas': mangas})

def manga_list(request):
    mangas = Manga.objects.all()
    return render(request, 'blog/manga_list.html', {'mangas': mangas})

def detail(request, manga_id):
    manga = get_object_or_404(Manga, pk=manga_id)
    return render(request, 'blog/detail.html', {'manga': manga})

def chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return render(request, 'blog/chapter.html', {'chapter': chapter})

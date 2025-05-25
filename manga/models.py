from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.manga.title} - {self.title}'

class Page(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='pages')
    image = models.ImageField(upload_to='pages/')
    page_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['page_number']

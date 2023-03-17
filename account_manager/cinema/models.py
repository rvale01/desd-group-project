from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    
    class Meta:
        app_label = 'cinema'
    def create(self, title, release_year, genre, description):
        film = self(title=title, release_year=release_year, genre=genre, description=description)
        film.save()
        return film

    def __str__(self):
        return self.title
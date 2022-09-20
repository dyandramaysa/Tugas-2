from django.db import models

# Create your models here.
class WatchList(models.Model):
    watched = models.CharField(max_length=50) #mendeskripsikan film tersebut sudah ditonton atau belum
    title = models.CharField(max_length=50) #mendeskripsikan judul film
    rating = models.IntegerField() #mendeskripsikan rating film dalam rentang 1 sampai dengan 5
    release_date = models.DateField() #mendeskripsikan kapan film dirilis
    review = models.TextField() #mendeskripsikan review untuk film tersebut

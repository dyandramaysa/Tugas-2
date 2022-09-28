from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Menghubungkan task dengan pengguna yang membuat task tersebut
    date = models.DateField(auto_now=True) # Mendeskripsikan tanggal pembuatan task
    title = models.CharField(max_length=100) # Mendeskripsikan judul task
    description = models.TextField() # Mendeskripsikan deskripsi task
    is_finished = models.BooleanField(default=False)
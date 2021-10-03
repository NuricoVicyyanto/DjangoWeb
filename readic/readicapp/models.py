from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cover/')

class Genre(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Artikel(models.Model):
    judul = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=50)
    konten = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    #jumlah = models.IntegerField(null=True) *buat nambah kolom tabel

    def __str__(self):
        return self.judul

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)

class jumbotron(models.Model):
    judul = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cover/')

    def __str__(self):
        return self.judul

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

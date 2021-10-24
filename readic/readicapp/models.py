from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from sklearn.tree import DecisionTreeClassifier
import joblib
# Create your models here.


#data
GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)
#ml
class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(
    validators=[MinValueValidator(13), MaxValueValidator(19)], null=True)
    height = models.PositiveIntegerField(null=True)
    sex = models.PositiveIntegerField(choices=GENDER, null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml/ml_model.joblib')
        self.predictions = ml_model.predict(
            [[self.age, self.height, self.sex]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name


class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')

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
    cover = models.ImageField(upload_to='image/', null=True)
    #jumlah = models.IntegerField(null=True) *buat nambah kolom tabel

    def __str__(self):
        return self.judul

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)

class jumbotron(models.Model):
    judul = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.judul

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

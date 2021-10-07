from readicapp.models import Artikel
from rest_framework import serializers

class ArtikelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikel
        fields = ['id', 'judul', 'deskripsi', 'genre_id', 'cover']
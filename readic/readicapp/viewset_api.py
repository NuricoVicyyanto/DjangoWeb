from readicapp.models import Artikel
from readicapp.serializers import ArtikelSerializer
from rest_framework import viewsets

class ArtikelViewset(viewsets.ModelViewSet):
    queryset = Artikel.objects.all()
    serializer_class = ArtikelSerializer


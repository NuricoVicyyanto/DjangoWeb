from import_export import resources
from readicapp.models import Artikel

class ArtikelResource(resources.ModelResource):
    class Meta:
        model = Artikel
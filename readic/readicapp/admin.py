from django.contrib import admin
from readicapp.models import *

# Register your models here. (buat nampilin semua form di admin)
class ArtikelAdmin(admin.ModelAdmin):
    list_display=['judul', 'deskripsi', 'genre_id', 'cover']
    search_fields=['judul', 'deskripsi']
    list_filter=['genre_id']
    list_per_page = 4


admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Genre),
admin.site.register(jumbotron)
admin.site.register(Profile)
admin.site.register(Data)


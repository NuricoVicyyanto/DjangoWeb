from django.forms import ModelForm, widgets
from django import forms
from readicapp.models import *

class FormArtikel(ModelForm):
    class Meta:
        model = Artikel
        fields = '__all__'
        #exclude = ['judul'] * untuk kolom yang tidak akan ditampilkan

        widgets = {
            'judul':forms.TextInput({'class':'form-control', 'id':'Judul'}),
            'deskripsi':forms.TextInput({'class':'form-control'}),
            'konten':forms.Textarea({'class':'form-control'}),
            'genre_id':forms.Select({'class':'form-control'}),
            'cover':forms.FileInput({'class':'form-control'})
        }

class FormGenre(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        #exclude = ['judul'] * untuk kolom yang tidak akan ditampilkan

        widgets = {
            'nama':forms.TextInput({'class':'form-control', 'id':'Nama'}),
            'keterangan':forms.TextInput({'class':'form-control'}),
        }

class FormJumbotr(ModelForm):
    class Meta:
        model = jumbotron
        fields = '__all__'
        #exclude = ['judul'] * untuk kolom yang tidak akan ditampilkan

        widgets = {
            'judul' : forms.TextInput({'class':'form-control', 'id':'Judul'}),
            'image' : forms.FileInput({'class':'form-control'})
        }
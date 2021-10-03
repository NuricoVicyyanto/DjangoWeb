from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from readicapp.models import *
from readicapp.forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from readicapp.resource import ArtikelResource
import os

#download excel sementara
def export_xls(request):
    artikel = ArtikelResource()
    dataset = artikel.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition']='attachment; filename=artikel.xls'
    return response

# Create your views here.
def home(request):
    jumbotr = jumbotron.objects.all()
    artikel = Artikel.objects.all()
    konteks = {
        'artikel' : artikel,
        'jumbotr' : jumbotr,
    }
    return render(request, 'frontend/home.html', konteks)

def read_artikel(request, id_artikel):
    artikel = Artikel.objects.get(id=id_artikel)
    template = 'frontend/read_artikel.html'
    form = FormArtikel(instance=artikel)
    konteks ={
            'form':form,
            'artikel':artikel,
        }
    return render(request, template, konteks)

def info(request):
    artikel = Artikel.objects.all()
    konteks = {
        'artikel' : artikel,
    }

    return render(request, 'frontend/info.html', konteks)

def about(request):
    return render(request, 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')


#backend auth
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun Berhasil Dibuat')
            return redirect('signup')
        else:
            messages.error(request, 'Terjadi Kesalahan')
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form' : form,
        }
    return render(request, 'registration/signup.html', konteks)



#backend function
@login_required(login_url=settings.LOGIN_URL)
def artikel(request):
    artikel = Artikel.objects.all()

    konteks ={
        'artikel':artikel,
    }

    return render(request, 'backend/artikel.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def add_artikel(request):
    if request.POST:
        form = FormArtikel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormArtikel

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/add_artikel.html', konteks)

    else:
        form = FormArtikel()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/add_artikel.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def change_artikel(request, id_artikel):
    artikel = Artikel.objects.get(id=id_artikel)
    template = 'backend/change_artikel.html'
    if request.POST:
        form = FormArtikel(request.POST,request.FILES, instance=artikel)
        if form.is_valid():
            form.save()
            return redirect('change_artikel', id_artikel=id_artikel)
    else:
        form = FormArtikel(instance=artikel)
        konteks ={
            'form':form,
            'artikel':artikel,
        }
        return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def delete_artikel(request, id_artikel):
    artikel = Artikel.objects.get(id=id_artikel)
    artikel.delete()

    return redirect('artikel')


#genre crud
@login_required(login_url=settings.LOGIN_URL)
def genre(request):
    genre = Genre.objects.all()

    konteks ={
        'genre':genre,
    }

    return render(request, 'backend/genre.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def add_genre(request):
    if request.POST:
        form = FormGenre(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormGenre

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/add_genre.html', konteks)

    else:
        form = FormGenre()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/add_genre.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def change_genre(request, id_genre):
    genre = Genre.objects.get(id=id_genre)
    template = 'backend/change_genre.html'
    if request.POST:
        form = FormGenre(request.POST,request.FILES, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('change_genre', id_genre=id_genre)
    else:
        form = FormGenre(instance=genre)
        konteks ={
            'form':form,
            'genre':genre,
        }
        return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def delete_genre(request, id_genre):
    genre = Genre.objects.get(id=id_genre)
    genre.delete()

    return redirect('genre')


#jumbotron crud
@login_required(login_url=settings.LOGIN_URL)
def jumbotr(request):
    jumbotr = jumbotron.objects.all()
    konteks ={
        'jumbotr':jumbotr,
    }

    return render(request, 'backend/jumbotr.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def add_jumbotr(request):
    if request.POST:
        form = FormJumbotr(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormJumbotr

            konteks={
                'form':form,
                'alert':alert,
            }
            return render(request, 'backend/add_jumbotr.html', konteks)

    else:
        form = FormJumbotr()
        konteks ={
            'form':form,
        }

    return render(request, 'backend/add_jumbotr.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def change_jumbotr(request, id_jumbotr):
    jumbotr = jumbotron.objects.get(id=id_jumbotr)
    template = 'backend/change_jumbotr.html'
    if request.POST:
        form = FormJumbotr(request.POST,request.FILES, instance=jumbotr)
        if form.is_valid():
            form.save()
            return redirect('change_jumbotr', id_jumbotr=id_jumbotr)
    else:
        form = FormJumbotr(instance=jumbotr)
        konteks ={
            'form':form,
            'jumbotr':jumbotr,
        }
        return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def delete_jumbotr(request, id_jumbotr):
    genre = jumbotron.objects.get(id=id_jumbotr)
    genre.delete()

    return redirect('jumbotr')
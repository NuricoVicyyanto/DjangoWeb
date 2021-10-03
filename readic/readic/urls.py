"""readic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from readicapp.views import *
from readicapp import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/read_artikel/<int:id_artikel>', read_artikel, name='read_artikel'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    #backend
    #artikel
    path('add_artikel/', add_artikel, name='add_artikel'),
    path('artikel/', artikel, name='artikel'),
    path('artikel/change_artikel/<int:id_artikel>', change_artikel, name='change_artikel'),
    path('artikel/delete_artikel/<int:id_artikel>', delete_artikel, name='delete_artikel'),

    #genre
    path('add_genre/', add_genre, name='add_genre'),
    path('genre/', genre, name='genre'),
    path('genre/change_genre/<int:id_genre>', change_genre, name='change_genre'),
    path('genre/delete_genre/<int:id_genre>', delete_genre, name='delete_genre'),

    #jumbotron
    path('add_jumbotr/', add_jumbotr, name='add_jumbotr'),
    path('jumbotr/', jumbotr, name='jumbotr'),
    path('jumbotr/change_jumbotr/<int:id_jumbotr>', change_jumbotr, name='change_jumbotr'),
    path('jumbotr/delete_jumbotr/<int:id_jumbotr>', delete_jumbotr, name='delete_jumbotr'),


    #autentifikasi
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),

    #unduh excel
    path('export/xls/', export_xls, name='export_xls'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
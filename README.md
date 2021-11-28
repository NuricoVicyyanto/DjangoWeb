# Go Go Go Learn Python

# django-admin startproject readic
# django-admin startapp readicapp
-di setting.py installed app tambah nama app
-pada folder utama buat folder templates untuk tempat kerangka html
-pada folder apps buat folder tempalte untuk tempat tampilan utama html
-tambahkan pada setting.templates.tempalte.dir 'templates'
-pada setting bagian paling bawah tambah STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
], folder static untuk membuat tempat bootsrap css dan jquery
-url->views, url untuk menandefinisikan route yang mengambil view dari views url(path('buku/', buku)), dan pada 
views (def buku(request):
    return render(request, 'buku.html'))
-membuat forms.py di folder apps luar

-python manage.py migrate
-python manage.py makemigrations
-python manage.py createsuperuser

-pip install django-cleanup 
INSTALLED_APPS = (
    ...,
    'django_cleanup.apps.CleanupConfig',
)





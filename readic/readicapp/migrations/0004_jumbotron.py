# Generated by Django 3.1.5 on 2021-09-30 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readicapp', '0003_artikel_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='jumbotron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='cover/')),
            ],
        ),
    ]

# Generated by Django 3.1.5 on 2021-10-01 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readicapp', '0004_jumbotron'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='konten',
            field=models.TextField(),
        ),
    ]

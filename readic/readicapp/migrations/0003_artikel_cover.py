# Generated by Django 3.1.5 on 2021-09-30 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readicapp', '0002_auto_20210930_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
    ]
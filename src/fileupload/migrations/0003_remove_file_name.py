# Generated by Django 4.0 on 2021-12-19 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]

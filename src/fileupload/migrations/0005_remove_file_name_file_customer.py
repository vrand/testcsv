# Generated by Django 4.0 on 2021-12-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0004_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AddField(
            model_name='file',
            name='customer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

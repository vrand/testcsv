# Generated by Django 4.0 on 2021-12-23 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0009_deliveryfile_uploadedfile_orderfile_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryfile',
            name='uploadedfile',
            field=models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.CASCADE, to='fileupload.file'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0007_file_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryfile',
            name='poids_total',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='deliveryfile',
            name='poids_unitaire',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='deliveryfile',
            name='prix_total',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='deliveryfile',
            name='prix_unitaire',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='poids_total',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='poids_unitaire',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='prix_total',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='prix_unitaire',
            field=models.IntegerField(blank=True),
        ),
    ]

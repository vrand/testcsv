from django.db import models
from django.template.defaultfilters import slugify
from rest_framework import serializers

PROFILE_CHOICES = [
    ('Profile 1', 'Client'),
    ('Profile 2', 'Transporteur'),
]


# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(blank=True, max_length=100)
    profile = models.CharField(max_length=20, choices=PROFILE_CHOICES, null=True)


class OrderFile(models.Model):
    uploadedfile = models.ForeignKey(File, on_delete=models.CASCADE, default=1)
    ean = models.CharField(max_length=50)
    designation = models.TextField(blank=True)
    reference = models.CharField(max_length=200)
    quantite = models.IntegerField()
    prix_unitaire = models.IntegerField(blank=True)
    prix_total = models.IntegerField(blank=True)
    poids_unitaire = models.IntegerField(blank=True)
    poids_total = models.IntegerField(blank=True)
    composition = models.TextField(blank=True)
    origine = models.IntegerField(blank=True)
    nomenclature_douaniere = models.CharField(max_length=50)
    reference_transport = models.CharField(max_length=50)


class DeliveryFile(models.Model):
    uploadedfile = models.ForeignKey(File, on_delete=models.CASCADE, default=1, db_constraint=False)
    ean = models.CharField(max_length=50)
    designation = models.TextField(blank=True)
    reference = models.CharField(max_length=200)
    quantite = models.IntegerField()
    prix_unitaire = models.IntegerField(blank=True)
    prix_total = models.IntegerField(blank=True)
    poids_unitaire = models.IntegerField(blank=True)
    poids_total = models.IntegerField(blank=True)
    composition = models.TextField(blank=True)
    origine = models.IntegerField(blank=True)
    nomenclature_douaniere = models.CharField(max_length=50)
    reference_transport = models.CharField(max_length=50)

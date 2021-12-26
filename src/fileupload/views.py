from django.views.generic import TemplateView, ListView, FormView
from rest_framework import viewsets, generics
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from .forms import CompareFormClient
from .models import OrderFile, DeliveryFile
from .serializer import FileUploadSerializer, SaveFileSerializer
import pandas as pd


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        file = request.data['file']
        profile = request.data['profile']
        print(profile)

        if serializer.is_valid():
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)

                if profile == "Client":
                    for i, row in df.iterrows():
                        new_file = OrderFile.objects.create(
                            ean=row['EAN'],
                            designation=row['Désignation'],
                            reference=row['Référence'],
                            quantite=row['Quantité'],
                            prix_unitaire=row['Prix Unitaire HT'],
                            prix_total=row['TOTAL HT'],
                            poids_unitaire=row['Poids unitaire (gr)'],
                            poids_total=row['Poids total (gr)'],
                            composition=row['Composition'],
                            origine=row['Origine'],
                            nomenclature_douaniere=row['Nomenclature douanière'],
                            reference_transport=row['Référence transport'],
                        )
                    serializer.save()

                elif profile == "Transporteur":
                    for i, row in df.iterrows():
                        new_file = DeliveryFile.objects.create(
                            ean=row['EAN'],
                            designation=row['Désignation'],
                            reference=row['Référence'],
                            quantite=row['Quantité'],
                            prix_unitaire=row['Prix Unitaire HT'],
                            prix_total=row['TOTAL HT'],
                            poids_unitaire=row['Poids unitaire (gr)'],
                            poids_total=row['Poids total (gr)'],
                            composition=row['Composition'],
                            origine=row['Origine'],
                            nomenclature_douaniere=row['Nomenclature douanière'],
                            reference_transport=row['Référence transport'],
                        )
                    serializer.save()
                else:
                    raise ValueError("Nothing happened")

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeView(ListView):
    template_name = "fileupload/index.html"
    title = "Default"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

    def get_queryset(self):
        return models.OrderFile.objects.all()


class CompareView(FormView):
    form_class = CompareFormClient
    title = "Default"
    template_name = "fileupload/compare.html"
    fields = ['ean', 'designation']
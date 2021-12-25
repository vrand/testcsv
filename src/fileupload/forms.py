from django.forms import forms

from fileupload.models import OrderFile, DeliveryFile


class CompareFormClient(forms.Form):
    class Meta:
        model = OrderFile
        fields = ["designation", "prix_total", ]


class CompareFormTransporteur(forms.Form):
    class Meta:
        model = DeliveryFile
        fields = ["designation", "prix_total", ]

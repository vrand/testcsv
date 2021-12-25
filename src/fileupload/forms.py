from django.forms import ModelForm

from fileupload.models import OrderFile, DeliveryFile


class CompareFormClient(ModelForm):
    # title = forms.CharField()
    # description = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = OrderFile
        fields = [
            "ean",
            "designation",
        ]

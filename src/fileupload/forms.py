from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms
from fileupload.models import OrderFile, DeliveryFile


class CompareFormClient(forms.ModelForm):
    class Meta:
        model = OrderFile
        fields = ['ean', 'designation']

    items = forms.ModelMultipleChoiceField(
        widget=FilteredSelectMultiple(
            'items',
            False,
        ),
        queryset=OrderFile.objects.all().values_list('reference', flat=True)
    )

    class Media:
        css = {
            'all': ['admin/css/widgets.css',
                    'css/uid-manage-form.css'],
        }
        # Adding this javascript is crucial
        js = ['/admin/jsi18n/']

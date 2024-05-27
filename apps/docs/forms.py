from django import forms
from django.forms import ModelForm

from .models import (
    Doc
)


class DocForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Doc
        fields = ['current_status', 'employee', 'doc_type', 'serial', 'number', 'date_of_issue', 'issued_authority', 'address', 'others', 'scanned_doc']

        # fields = ['date', 'description']

        # widgets = {
        #     'date': forms.DateInput(
        #         format=('%d.%m.%Y'),
        #         attrs={'class': 'form-control', 
        #                'placeholder': 'Select a date',
        #                'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #               })
        # }
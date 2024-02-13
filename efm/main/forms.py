from django import forms
from .models import Catalog


class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CatalogForm, self).__init__(*args, **kwargs)
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['patronymic'].widget.attrs.update({'class': 'form-control'})
        self.fields['organisation'].widget.attrs.update({'class': 'form-control'})
        self.fields['work_phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['personal_phone'].widget.attrs.update({'class': 'form-control'})
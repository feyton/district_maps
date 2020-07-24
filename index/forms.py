from django import forms
from .models import District, ShapeImage
from django.forms import SelectMultiple, Textarea


class ShapeImageForm(forms.ModelForm):
    class Meta:
        model = ShapeImage
        exclude = ['code', 'slug', 'image', ]
        widgets = {
            'summary': Textarea(attrs={'rows': 3, 'cols': 60, 'class': 'form-control'}),
            'districts': SelectMultiple(attrs={'class': 'selectpicker form-control', 'data-style': "btn-info", 'data-size': "5"})
        }


class OptionForm(forms.Form):
    show_title = forms.CheckboxInput()

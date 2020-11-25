from django import forms
from .models import ShapeImage, ShapeDeleteRequest
from django.forms import SelectMultiple, Textarea


class ShapeImageForm(forms.ModelForm):
    class Meta:
        model = ShapeImage
        exclude = ['code', 'slug', 'image', 'download_name']
        widgets = {
            'summary': Textarea(attrs={'rows': 3, 'cols': 60, 'class': 'form-control'}),
            'districts': SelectMultiple(attrs={'class': 'selectpicker form-control', 'data-style': "btn-info", 'data-size': "5"})
        }


class OptionForm(forms.Form):
    colors = (('c', 'Cyan'), ('b', 'Blue'), ('g', 'Green'))
    color = forms.ChoiceField(choices=colors, required=False, initial='b')
    show_title = forms.BooleanField(initial=True)
    add_name = forms.BooleanField(initial=True)


class DeleteShapeForm(forms.ModelForm):
    class Meta:
        model = ShapeDeleteRequest
        exclude = ['date', 'shape', ]

from django import forms
from django.core.validators import RegexValidator, URLValidator, MinValueValidator

from .models import Furniture


class FurnitureForm(forms.ModelForm):
    choices = list(Furniture.KIND_MATERIAL)
    model = forms.CharField(required=True, widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control'
                               }
                           ))
    make = forms.CharField(required=True,
                           validators=[RegexValidator(r'^[A-Z][a-z]+$', message="Furnitur's name must start with capital latain letter, followed by latain small letters.")],
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control'
                               }
                           ))
    description = forms.CharField(required=True,
                            widget=forms.Textarea(
                                  attrs={
                                      'class': 'form-control'
                                  }
                                  ))
    price = forms.IntegerField(required=True,
                             min_value=0,
                             validators=[RegexValidator(r'^\d+$', message='The age must be positive number ot 0')],
                             widget=forms.NumberInput(
                                 attrs = {
                                     'class': 'form-control'
                                 }
                             ))
    image_url = forms.URLField(required=True,
                               widget=forms.TextInput(
                                   attrs= {
                                       'class': 'form-control'
                                   }
                               ))
    material = forms.ChoiceField(choices=choices,
                                widget=forms.Select(
                                    attrs= {
                                        'class': 'form-control'
                                    }
                                )
                             )

    class Meta:
        model = Furniture
        fields = ('make', 'model', 'description', 'price', 'image_url', 'material')

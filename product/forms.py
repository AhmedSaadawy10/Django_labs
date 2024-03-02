from django import forms
from .models import product
from categories.models import *


class ProductForm(forms.Form):
    name=forms.CharField(max_length=20)
    model = forms.IntegerField(label='Product Model', required=False)
    price = forms.IntegerField(label='Product Price', required=False)
    type = forms.CharField(label='Product Type', required=False)
    image = forms.ImageField(required=False)
    category=forms.ChoiceField(choices=[(i.id, i.name) for i in Category.objects.all()])

    def clean_name(self):
        name = self.cleaned_data['name']
        if product.objects.filter(name=name).exists():
            raise forms.ValidationError("name already exists")
        return name



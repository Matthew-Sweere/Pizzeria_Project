from django import forms

from .models import Pizza
from .models import Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name': ''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name': 'Topping:'}
        # A widget is an HTML form element, such as a single-line text box,
        # a multi-line text area, or drop-down list.
        # customize the input widget for the field 'text' so the text area
        # will be 80 columns wide instead of the default 40
        widgets = {'name': forms.Textarea(attrs={'cols': 80})}
    
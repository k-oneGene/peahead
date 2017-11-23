from django import forms

from .models import Quotes


class QuotesForm(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = [
                'name',
                'quote'
                ]


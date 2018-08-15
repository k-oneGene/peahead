from django import forms

from .models import Quotes


class QuotesForm(forms.ModelForm):

    class Meta:
        model = Quotes
        fields = [
                'name',
                'quote'
                ]

    def __init__(self, *args, **kwargs):
        super(QuotesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['quote'].widget.attrs.update({'class': 'form-control'})

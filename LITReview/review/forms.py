from django import forms
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Ticket

# class TicketForm(forms.Form):
#     title = forms.CharField(max_length=128, required=True)
#     description = forms.CharField(max_length=128, required=True, widget=forms.Textarea())

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

        labels = {"title": "Titre",
                  "description": "Description"
                  }
        # widgets = {"description": forms.Textarea()}


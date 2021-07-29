from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', "image"]

        labels = {"title": "Titre",
                  "description": "Description"
                  }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        labels = {"headline": "Titre de la critique",
                  "rating": "Note",
                  "body": "Commentaire"
                  }
        CHOICES = [(0, '0'),
                   (1, '1'),
                   (2, '2'),
                   (4, '3'),
                   (4, '4'),
                   (5, '5')
                   ]
        widgets = {"rating": forms.RadioSelect(choices=CHOICES),
                   "body": forms.Textarea()
                   }

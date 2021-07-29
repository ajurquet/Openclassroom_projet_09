from django import forms
from django.contrib.auth.models import User

from .models import UserFollows


class SubscriptionsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']
        labels = {"followed_user": ""}
        widgets = {'followed_user': forms.TextInput()}

        def clean_followed_user(self):
            followed_user = self.cleaned_data['followed_user']
            user = User.objects.get(id=self.request.user.id)
            if followed_user == user:
                raise ValueError('Vous ne pouvez pas vous ajouter')
            return followed_user

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import UserFollows


class SubscriptionsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['user']
        widgets = {'user': models.CharField(max_length=128, blank=False)}

        
        
    # def clean_followed_user:
    #     followed_user = followed_user.objects.exclude(id=request.user.id)

# class SubscriptionsForm(forms.Form):
#     title = forms.CharField(max_length=128, required=True)
#     description = forms.CharField(max_length=128, required=True, widget=forms.Textarea())


# class SubscriptionsForm(forms.Form):
#     # user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
#     # followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')
#     user = forms.CharField(max_length=128, required=True)
#     followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

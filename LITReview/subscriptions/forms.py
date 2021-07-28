from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django import forms

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
            print(user)
            if followed_user == user:
                raise ValueError('Vous ne pouvez pas vous ajouter')
            return followed_user


# class SubscriptionDeleteView(LoginRequiredMixin,
                            
#                             DeleteView,
#                             SuccessMessageMixin
#                             ):
#     model = UserFollows
#     success_url = reverse_lazy('subscriptions')
#     success_message = "Abonnement résilié"

    
#     def get_context_data(self, **kwargs):
#         context  = super().get_context_data(**kwargs)
#         current_user = User.objects.get(id=self.request.user.id)
#         print(current_user)
#         print(context)
#         context['followed_user'] = UserFollows.objects.exclude(user=current_user)
#         print(context)
        
#         return context


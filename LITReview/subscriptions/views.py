from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import SubscriptionsForm
from .models import UserFollows


@login_required
def subscriptions(request):
    title = "Onglet d'abonnements"
    users = User.objects.all()
    user_follows = UserFollows.objects.all()
    user = request.user
    subscribers = user.followed_by.all()

    if request.method == "POST":
        try:
            entry = request.POST['followed_user']
            user_to_follow = User.objects.get(username=entry)

            for u in users:
                if u.username == entry:
                    UserFollows.objects.create(user=request.user,
                                               followed_user=user_to_follow,
                                               )
        except Exception:
            form = SubscriptionsForm(request.POST)
            messages.error(request, 'Erreur')
        else:
            messages.success(request, "Utilisateur suivi !")
            return redirect("subscriptions")
    else:
        form = SubscriptionsForm()

    return render(request, 'subscriptions/subscriptions.html', {
                                                'title': title,
                                                'form': form,
                                                'current_user': user,
                                                'subscribers': subscribers,
                                                'user_follows': user_follows
                                                })


class SubscriptionDeleteView(LoginRequiredMixin,
                             DeleteView,
                             SuccessMessageMixin
                             ):
    model = UserFollows
    success_url = reverse_lazy('subscriptions')
    success_message = "Abonnement résilié"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = User.objects.get(id=self.request.user.id)
        context['followed_user'] = UserFollows.objects.exclude(
                                                            user=current_user)
        return context

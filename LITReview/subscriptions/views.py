from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
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
    followers = user.following.all()
    subscribers = user.followed_by.all()
     
    if request.method == "POST":
        try:
            entry = request.POST['followed_user']
            user_to_follow = User.objects.get(username=entry)
            
            for u in users:
                if u.username == entry:
                    UserFollows.objects.create(user=request.user,
                                               followed_user = user_to_follow,
                                               )
        except:
            form = SubscriptionsForm(request.POST)
            messages.error(request, f'Erreur')  
        else:
            messages.success(request, "Utilisateur suivi !")
            return redirect("subscriptions")
    else:
        form = SubscriptionsForm()
        
    return render(request, 'subscriptions/subscriptions.html', {
                                                    'title' : title,
                                                    'form': form,
                                                    'users': users,
                                                    'current_user': user,
                                                    'followers' : followers,
                                                    'subscribers': subscribers,
                                                    'user_follows': user_follows
                                                     })


# @login_required
# def unsubscribe(request, userfollow_id):
#     title = "Se désabonner"
#     userfollow_instance = UserFollows.objects.get(pk=userfollow_id)
    
#     return render(request, 'subcriptions/userfollows_confirm_delete.html',{
#                                             "title" : title,
#                                             "instance": userfollow_instance
                                            
#                                             })


class SubscriptionDeleteView(LoginRequiredMixin,
                            UserPassesTestMixin,
                            DeleteView,
                            SuccessMessageMixin
                            ):
    model = UserFollows
    success_url = reverse_lazy('subscriptions')
    success_message = "Abonnement résilié"

    def test_func(self):
        user_follow = self.get_object()
        if self.request.user == user_follow.user:
            return True
        return False


    # users_to_follow = User.objects.exclude(id=request.user.id)

    # users_followed = User.objects.all()
    # users_followed = users_followed.following.all()

    # users_subscribes_user = User.objects.all()
    # users_subscribes_user = users_subscribes_user.followed_by.all()



# class SubscriptionCreate(CreateView):
#     model = UserFollows
#     form_class = SubscriptionsForm

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request, "subscriptions/userfollows_form.html", {'form': form})


    


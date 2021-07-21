from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic

from .forms import SubscriptionsForm
from .models import UserFollows


@login_required
def subscriptions(request):
    title = "Onglet d'abonnements"
     
    if request.method == "POST":
        try:
            users = User.objects.all()
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
            # messages.success(request, "Utilisateur suivi !")
            return redirect("subscriptions")

    else:
        form = SubscriptionsForm()

    return render(request, 'subscriptions/subscriptions.html', {'title' : title,
                                                        'form': form,
                                                        })

   
    # users_to_follow = User.objects.exclude(id=request.user.id)

    # users_followed = User.objects.all()
    # users_followed = users_followed.following.all()

    # users_subscribes_user = User.objects.all()
    # users_subscribes_user = users_subscribes_user.followed_by.all()

class UserFollowsListView(generic.ListView):
    model = UserFollows

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(UserFollowsListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


    


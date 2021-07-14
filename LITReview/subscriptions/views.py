from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import SubscriptionsForm
from .models import UserFollows


@login_required
def subscriptions(request):
    title = "Onglet d'abonnements"
    
    users_to_follow = User.objects.exclude(id=request.user.id)

    users_followed = User.objects.all()
    users_followed = users_followed.following.all()

    users_subscribes_user = User.objects.all()
    users_subscribes_user = users_subscribes_user.followed_by.all()

    
    if request.method == "POST":
        try:
            UserFollows.objects.create(user=request.POST['user'],
                            followed_user = request.POST['followed_user'],
                            )
            
        except:
            form = SubscriptionsForm(request.POST)
        else:
            # return render(request,'review/flux.html')
            return redirect("subscriptions")

    else:
        form = SubscriptionsForm()

    return render(request, 'subscriptions/subscriptions.html', {'title' : title,
                                                        'form': form,
                                                        'users_followed': users_followed,
                                                        'users_subscribes_user': users_subscribes_user}
                                                        )

from django.contrib import messages
from django.contrib.messages.api import success
from django.urls.base import reverse
from review.models import Review, Ticket
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from operator import attrgetter
from itertools import chain
from django.db.models import CharField, Value

from .forms import TicketForm, ReviewForm
from .models import Ticket, Review


@login_required
def create_ticket(request):
    title = "Créer un ticket"
    
    if request.method == "POST":
        try:
            Ticket.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            image = request.FILES['image'],
                            user=request.user
                            )
        except:
            form = TicketForm(request.POST, request.FILES)
        else:
            messages.success(request, 'Ticket créé !')
            return redirect("flux")

    else:
        form = TicketForm(request.POST, request.FILES)

    return render(request, 'review/createticket.html', {'title' : title,
                                                        'form_ticket': form}
                                                        )


@login_required
def create_review(request):
    title = "Créer une review"

    if request.method == "POST":
        try:
            ticket_instance = Ticket.objects.create(title=request.POST['title'],
                                description=request.POST['description'],
                                image = request.FILES['image'],
                                user=request.user
                                )

            Review.objects.create(ticket=ticket_instance,
                            headline=request.POST['headline'],
                            rating=request.POST['rating'],
                            body=request.POST['body'],
                            user=request.user
                            )
        except:
            form = ReviewForm(request.POST)
        else:
            messages.success(request, f'Review créée !')
            return redirect("flux")

    else:
        form_review = ReviewForm()
        form_ticket = TicketForm()

    return render(request, 'review/createreview.html',{
                                                      'title' : title,
                                                      'form_review': form_review,
                                                      'form_ticket': form_ticket
                                                      })


@login_required
def flux(request):
    user = request.user
    
    # Queries on reviews
    users_to_exclude = []
    for r in Review.objects.all():
        if r.ticket.user == request.user:
            users_to_exclude.append(r.pk)

    print(users_to_exclude)

    # users1_to_exclude = []
    # for r in Review.objects.all():
    #     if r.ticket.user == request.user:
    #         users1_to_exclude.append(r.pk)
    # print(users1_to_exclude)

    reviews = Review.objects.filter(user=request.user).exclude(user_id__in=users_to_exclude) 
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))


    #Queries on tickets
    followers = user.following.all()
    print(f"followers : {followers}")

    followers_list = []
    for follower in followers:
        followers_list.append(follower.followed_user.pk)
    print(followers_list)

    tickets = Ticket.objects.filter(user_id__in=followers_list)
    print(tickets)
    tickets = Ticket.objects.filter(user=request.user)
    print(tickets)
    tickets = Ticket.objects.filter(user_id__in=followers_list).filter(user=request.user)
    print(tickets)

    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))


    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )

    return render(request, 'review/flux.html', context={'posts': posts})




# title = "Flux"
#     current_user = request.user
#     all_posts = [] 
#     tickets = Ticket.objects.filter().order_by('-time_created')
#     reviews = Review.objects.filter().order_by('-time_created')
#     for ticket in tickets:
#         all_posts.append(ticket)
#     for review in reviews:
#         all_posts.append(review)
#     print(all_posts)
#     all_posts.sort(key=attrgetter('time_created'), reverse=True)
#     print(all_posts)

#     context = {"tickets" : tickets,
#                "title" : title,
#                "current_user": current_user,
#                "reviews": reviews,
#                "all_posts": all_posts
#                }
#     return render(request, "review/flux.html", context)


   

    
@login_required
def posts(request):
    title = "Posts"
    current_user = request.user
    tickets = Ticket.objects.filter(user=current_user)
    for ticket in tickets:
        print(ticket.image)
    reviews = Review.objects.filter(user=current_user).filter()
    context = {"title": title,
               "tickets" : tickets,
               "reviews" : reviews,
               "current_user": current_user,
               }
    return render(request, "review/posts.html", context)


class TicketUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('posts')

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False


class TicketDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('posts')

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False


class ReviewUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('posts')

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class ReviewDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('posts')

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

from subscriptions.models import UserFollows
from django.contrib import messages
from review.models import Review, Ticket
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
def create_review_existing_ticket(request, id_ticket=None):
    title = "Créer une review"

    existing_ticket = Ticket.objects.get(pk=id_ticket)

    if request.method == "POST":
        try:                                
            Review.objects.create(ticket=existing_ticket,
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

    return render(request, 'review/createreview_existing_ticket.html',{
                                            'title' : title,
                                            'form_review': form_review,
                                            'existing_ticket': existing_ticket
                                            })


@login_required
def flux(request):
    current_user = request.user
    users_follows = UserFollows.objects.all()

    # Ids of all my followers
    followers = current_user.following.all()
    followers_id = []
    for follower in followers:
        followers_id.append(follower.followed_user.pk)

    reviews = Review.objects.filter()

    # Ids of users who answered my tickets
    user_tickets = Ticket.objects.filter(user=current_user)

    ids_of_ticket_answerers = []
    for ticket in Ticket.objects.filter(user=current_user):
        for review in Review.objects.all():
            if review.ticket == ticket:
                ids_of_ticket_answerers.append(review.user.pk)
    print(f'Ids des répondant : {ids_of_ticket_answerers}')

    test_reviews = Review.objects.filter(user=request.user) | Review.objects.filter(user_id__in=followers_id) 
    print(test_reviews)

    # Queries on reviews
    users_to_include = []
    for review in Review.objects.all():
        if review.user == request.user: # Si la review est l'utilisateur
            users_to_include.append(review.user.pk)
        if review.user == request.user.following: # Si la review est d'un des abonnés
            review.user.append(review.user.pk)
        if review.ticket.user == request.user: # Si le ticket est de l'utilisateur
            users_to_include.append(review.ticket.user.pk)

    reviews = Review.objects.filter(user=request.user) | Review.objects.filter(user_id__in=followers_id)| Review.objects.filter(user_id__in=ids_of_ticket_answerers)

    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))


    #Queries on tickets
    followers = current_user.following.all()
    followers_list = []
    for follower in followers:
        followers_list.append(follower.followed_user.pk)

    tickets = Ticket.objects.filter(user_id__in=followers_list) | Ticket.objects.filter(user=request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )

    for post in posts:
        print(post)

    return render(request, 'review/flux.html', context={'posts': posts})
 
    
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

from django.contrib import messages
from django.contrib.messages.api import success
from review.models import Review, Ticket
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


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
            # return render(request,'review/flux.html')
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

    return render(request, 'review/createreview.html', {'title' : title,
                                                        'form_review': form_review,
                                                        'form_ticket': form_ticket
                                                        })


@login_required
def flux(request):
    title = "Flux"
    current_user = request.user
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    context = {"tickets" : tickets,
               "title" : title,
               "current_user": current_user,
               "reviews": reviews,
               }
    return render(request, "review/flux.html", context)

    
@login_required
def posts(request):
    title = "Posts"
    current_user = request.user
    tickets = Ticket.objects.filter(user=current_user)
    reviews = Review.objects.filter(user=current_user)
    context = {"title": title,
               "tickets" : tickets,
               "reviews" : reviews,
               "current_user": current_user,
               }
    return render(request, "review/posts.html", context)


class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['title', 'description', 'image']
    # template = "review/templates/review/ticket_form.html"



class TicketDelete(DeleteView):
    model = Ticket
    success_url = reverse_lazy('posts')


class ReviewUpdate(UpdateView):
    model = Review
    fields = ['rating', 'headline', 'body']


class ReviewDelete(DeleteView):
    model = Review
    success_url = reverse_lazy('posts')


 # if request.method == "GET":
    #     form = ReviewForm()
    #     return render(request, "review/createreview.html", locals())

    # elif request.method == "POST":
    #     form = ReviewForm(request.POST)
    #     print(request.POST)
    #     if form.is_valid():
    #         print("form is valid")
    #         form.save()
    #         return redirect('flux')
    
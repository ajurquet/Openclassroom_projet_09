from review.models import Review, Ticket
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import TicketForm, ReviewForm


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
        # try:
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
        # except:
        #     form = ReviewForm(request.POST)
        # else:
            # return render(request,'review/flux.html')
        return redirect("flux")

    else:
        form_review = ReviewForm()
        form_ticket = TicketForm()

    return render(request, 'review/createreview.html', {'title' : title,
                                                        'form_review': form_review,
                                                        'form_ticket': form_ticket
                                                        })


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


@login_required
def flux(request):
    title = "Flux"
    current_user = request.user
    user_tickets = Ticket.objects.all()
    context = {
        "user_tickets" : user_tickets
    }
    return render(request, "review/flux.html", {"title" : title,
                                                "context": context}
                                                )

    

    
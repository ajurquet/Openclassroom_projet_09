from review.models import Ticket
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import TicketForm


@login_required
def createticket(request):
    title = "Créer un ticket"
    
    if request.method == "POST":
        try:
            Ticket.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            user=request.user
                            )
        except:
            form = TicketForm(request.POST)
        else:
            return render(request,'review/createticket.html')

    else:
        form = TicketForm()

    return render(request, 'review/createticket.html', {'title' : title, 'form': form})


@login_required
def flux(request):
    title = "Flux"
    current_user = request.user
    # user_tickets = Ticket.objects.get(user=current_user)
    user_tickets = Ticket.objects.all()
    context = {
        "user_tickets" : user_tickets
    }
    return render(request, "review/flux.html", {"title" : title, "context": context})

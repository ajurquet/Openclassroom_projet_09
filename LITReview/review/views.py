from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import TicketForm

@login_required
def createticket(request):
    title = "Créer un ticket"
    
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            
    # permet de garder les champs remplis si le formulaire n'est pas valide     
    else:
        form = TicketForm()

    return render(request, 'review/createticket.html', {'title' : title, "form": form})

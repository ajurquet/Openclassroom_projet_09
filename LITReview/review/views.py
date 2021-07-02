from django.shortcuts import render

from .models import Ticket

def createticket(request):
    title = "Créer un ticket"
    return render(request, 'review/createticket.html', {"title" : title})

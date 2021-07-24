from review.models import Review, Ticket
from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Review)




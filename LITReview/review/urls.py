from django.urls import path

from. import views

urlpatterns = [
    path('', views.createticket, name='create_ticket'),
]
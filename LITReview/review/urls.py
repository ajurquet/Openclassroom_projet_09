from django.urls import path

from. import views


urlpatterns = [
    path('/review', views.createticket, name='create_ticket'),
    path('', views.flux, name='flux'),
]
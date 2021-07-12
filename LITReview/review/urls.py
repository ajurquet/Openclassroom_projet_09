from django.urls import path

from. import views


urlpatterns = [
    path('', views.flux, name='flux'),
    path('createticket', views.create_ticket, name='create_ticket'),
    path('createreview', views.create_review, name='create_review')
]


from django.urls import path

from . import views


urlpatterns = [
    path('', views.flux, name='flux'),
    path('posts', views.posts, name='posts'),
    path('createticket', views.create_ticket, name='create_ticket'),
    path('createreview', views.create_review, name='create_review'),

    path('createreviewexistingticket/<int:id_ticket>/',
         views.create_review_existing_ticket,
         name='create_review_existing_ticket'
         ),
    path('ticket/<int:pk>/update',
         views.TicketUpdate.as_view(),
         name='ticket-update'
         ),
    path('ticket/<int:pk>/delete',
         views.TicketDelete.as_view(),
         name='ticket-delete'
         ),
    path('review/<int:pk>/update',
         views.ReviewUpdate.as_view(),
         name='review-update'
         ),
    path('review/<int:pk>/delete',
         views.ReviewDelete.as_view(),
         name='review-delete'
         )
]

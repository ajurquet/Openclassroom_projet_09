from django.urls import path
from .views import SubscriptionDeleteView

from. import views


urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('<int:pk>/delete',
         SubscriptionDeleteView.as_view(),
         name='subscriptions_delete')
]

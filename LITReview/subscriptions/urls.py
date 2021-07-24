from django.urls import path
# from .views import SubscriptionCreate

from. import views


urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    # path('', SubscriptionCreate.as_view(), name='subscriptions')
]

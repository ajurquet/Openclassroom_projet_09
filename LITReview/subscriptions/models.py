from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by', help_text="Utilisateur suivi")

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )

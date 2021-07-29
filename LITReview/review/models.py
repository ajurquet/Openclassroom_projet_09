from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Ticket(models.Model):
    # Your Ticket model definition goes here
    title = models.CharField(max_length=128, blank=False)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="ticket_pics")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ticket", kwargs={"pk": self.pk})


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)],
        verbose_name='Note')
    headline = models.CharField(max_length=128, verbose_name='Titre')
    body = models.TextField(max_length=8192,
                            blank=True,
                            verbose_name='Description'
                            )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("review", kwargs={"pk": self.pk})

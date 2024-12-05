from django.db import models
from django.urls import reverse

class Capitals(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country} : {self.city}"

    def get_absolute_url(self):
        return reverse("home")

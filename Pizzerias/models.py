from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Pizza(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f"{self.name[:50]}..."

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."
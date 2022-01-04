from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    """Pizza names"""
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return pizza's names"""
        return self.name


class Topping(models.Model):
    """Topping names in pizza"""
    pizza_name = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='toppings',null=True)
    topping = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return pizza's topping"""
        return f"{self.topping}"

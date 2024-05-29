from django.db import models
from django.db.models import Model
import uuid


# Create your models here.

class Ticket(Model):
    id = models.CharField(primary_key=True, max_length=64)
    destination = models.CharField(max_length=256)
    price = models.FloatField()

    def __str__(self):
        # return '{0}. {1}: cena:{2} Kč'.format(self.poradi, self.nazev, self.cena)
        # return str(self.nazev)
        return f"{self.id}, Vybraná destinace: {self.destination}, cena: {self.price} Kč"


class Order(Model):
    id = models.CharField(primary_key=True, max_length=64)
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    email = models.EmailField(blank=False, default=None)
    amount = models.IntegerField(default=1)
    total = models.FloatField(null=True, default=float(0))
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=1)

    def __str__(self):
        # return '{0}. {1}: cena:{2} Kč'.format(self.poradi, self.nazev, self.cena)
        # return str(self.nazev)
        return f"Order: {self.id} for {self.last_name}, destinace: {self.ticket.destination}, email: {self.email}"

    def total(self):
        return self.amount * self.ticket.price
from django.db import models
from login.models import Member

# Create your models here.

class Player(models.Model):
    balance = models.FloatField()
    member = models.OneToOneField(Member,
                                  on_delete=models.CASCADE,
                                  related_name="player")
    def increment_balance(self):
        self.balance += 1
        self.save()

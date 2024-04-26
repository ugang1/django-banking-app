from django.db import models
from django.contrib.auth.models import User


class Bankapp(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bankapp {self.account_number}-{self.user.username }"

class Transaction(models.Model):
    Bankapp = models.ForeignKey(Bankapp, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type   = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} {self.amount} {self.timestamp}"
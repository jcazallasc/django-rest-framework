from django.conf import settings
from django.db import models


class Transaction(models.Model):
    """Transaction to be used for user"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    reference = models.CharField(max_length=255, unique=True)
    account = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

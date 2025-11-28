from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=False)
    email_address = models.EmailField(default="", max_length=254)
    account = models.FloatField(blank=True, null=True)
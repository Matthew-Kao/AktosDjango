from django.db import models

class Consumer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255) 

class Account(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    client_reference_no = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
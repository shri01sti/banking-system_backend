from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Customer(models.Model):
    customerId = models.AutoField(primary_key = True, null = False)
    name = models.CharField(max_length = 50, null = False)
    email = models.EmailField(null = True, blank = True)
    currentBalance = models.FloatField(null = True, blank = True)
    def __str__(self):
        return f'{self.customerId}'

class Transaction(models.Model):
    transactionId = models.AutoField(primary_key = True, null = False)
    transactionDate = models.DateField(null = True, blank = True, auto_now = True)
    customerToId = models.ForeignKey(Customer , null = False , on_delete= CASCADE, related_name = 'customerTo')
    customerById = models.ForeignKey(Customer, null = False, on_delete = CASCADE, related_name = 'customerBy' )
    transactionAmount = models.FloatField(null = False)
    def __str__(self):
        return f'{self.transactionId}'
    
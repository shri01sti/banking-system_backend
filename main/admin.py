from django.contrib import admin
from .models import Customer,Transaction


# Register your models here.
@admin.register(Customer)
class CustomerDisplay(admin.ModelAdmin):
    list_display = ('customerId','email','name','currentBalance') 

@admin.register(Transaction)
class TransactionDisplay(admin.ModelAdmin):
    list_display = ('transactionId','transactionDate','customerToId','customerById','transactionAmount')

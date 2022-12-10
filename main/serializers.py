
from rest_framework import serializers
from main.models import Customer, Transaction


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customerId','name','email','currentBalance')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transactionId', 'transactionDate', 'customerToId', 'customerById','transactionAmount')


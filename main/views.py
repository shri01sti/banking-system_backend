from django.shortcuts import render
from django.http import HttpResponse
from main.models import Customer, Transaction
from main.serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from main.serializers import TransactionSerializer


# Create your views here. 
def index(response):
    return HttpResponse('Hello')


'''  
returns all customer data from database
'''
@api_view(['GET'])
def getCustomers(request):
    customers = Customer.objects.all()
    serialized_data = CustomerSerializer(customers, many = True)
    
    return Response(serialized_data.data)


'''
add new customer 
if requested data is valid
else return error message
'''
@api_view(['POST'])
def postCustomer(request):
    new_customer = CustomerSerializer(data=request.data)
    if new_customer.is_valid():
        new_customer.save()

        return Response(new_customer.data)
    else:
        return Response(new_customer.errors, status = status.HTTP_400_BAD_REQUEST)


''' 
updating existing data
if requested data is valid
else return error message
'''
@api_view(['PUT'])
def updateCustomer(request,pk):
    existing_customer = Customer.objects.get(customerId = pk)
    updated_customer = CustomerSerializer(instance = existing_customer, data = request.data)

    if updated_customer.is_valid():
        updated_customer.save()

        return Response(updated_customer.data)
    else:
        return Response(updated_customer.errors, status = status.HTTP_400_BAD_REQUEST)


'''
delete requested data
if requested data exists
else return error message
'''  
@api_view(['DELETE'])
def deleteCustomer(request,pk):
    try:
        existing_customer = Customer.objects.get(customerId = pk)
        existing_customer.delete()

        return Response('Customer ' + pk + 'deleted successfully')
    except:
        return Response('Error detected' , status = status.HTTP_400_BAD_REQUEST)


'''
return all existing transactions
'''
@api_view(['GET'])
def getTransaction(request):
    transactions = Transaction.objects.all()
    serialized_data = TransactionSerializer(transactions, many = True)

    return Response(serialized_data.data)


'''
 add new transaction
if sender balance is enough to send to receiver and follow the consecutive transaction
else return error message
'''
@api_view(['POST'])
def postTransaction(request):
    sender_current_amt = Customer.objects.filter(customerId = request.data['customerById']).values_list('currentBalance',flat = True)[0]
    
    if (sender_current_amt <= request.data['transactionAmount']):
        return Response('insufficient balance',status = HTTP_400_BAD_REQUEST)
    
    
    new_transaction = TransactionSerializer(data = request.data)
    if new_transaction.is_valid():
        new_transaction.save()

        receiver_current_amt = Customer.objects.filter(customerId = request.data['customerToId']).values_list('currentBalance', flat = True)[0]

       # deducting balance of sender
        Customer.objects.filter(customerId = request.data['customerById']).update(currentBalance = sender_current_amt - new_transaction.data['transactionAmount']) 

        # adding balance on receiver
        Customer.objects.filter(customerId = request.data['customerToId']).update(currentBalance = receiver_current_amt + new_transaction.data['transactionAmount'])

        return Response(new_transaction.data)
    else:
        return Response(new_transaction.errors, status = status.HTTP_400_BAD_REQUEST)


'''
updating requested data
if requested data is valid
else return error message
'''
@api_view(['PUT'])
def updateTransaction(request,pk):
    existing_transaction = Transaction.objects.get(transactionId = pk)
    updated_transaction = TransactionSerializer(instance = existing_transaction, data = request.data)
    if updated_transaction.is_valid():
        updated_transaction.save()

        return Response(updated_transaction.data)
    else:
        return Response(updated_transaction.errors, status = status.HTTP_400_BAD_REQUEST)


'''
delete requested data
if requested data exists
else return error message
'''
@api_view(['DELETE'])
def deleteTransaction(request,pk):
    try:
        existing_transaction = Transaction.objects.get(transactionId = pk)
        existing_transaction.delete()
        return Response('Transaction ' + pk + 'deleted successfully')
    except:
        return Response('Error detected' , status = status.HTTP_400_BAD_REQUEST)








    

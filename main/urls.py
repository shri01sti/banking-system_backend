from django.urls import path
from main import views


urlpatterns = [
    path('', views.index,name = 'index'),
    path('customers', views.getCustomers, name = 'get_customers'),
    path('customer',views.postCustomer, name = 'post_customer'),
    path('customer/<str:pk>', views.updateCustomer, name = 'put_customer'),
    path('customer-del/<str:pk>', views.deleteCustomer, name = 'delete_customer'),
    path('transactions',views.getTransaction,name ='get_transaction'),
    path('transaction',views.postTransaction, name = 'post_transaction'),
    path('transaction-update/<str:pk>', views.updateTransaction, name ='put_transaction'),
    path('transaction-del/<str:pk>', views.deleteTransaction, name ='delete_transaction')

]
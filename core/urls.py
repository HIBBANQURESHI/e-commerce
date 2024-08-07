from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout_view, name='checkout'),   
    path('payment-completed/', views.payment_completed_view, name='payment-completed'),
    path('payment-failed/', views.payment_failed_view, name='payment-failed'),
    
]

from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm


def index(request):
    return render(request, 'core/index.html')

def checkout_view(request):
    host = request.get_host()
    total_amount = 200

    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            total_amount += int(item['qty']) * float(item['price'])
    
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '{:.2f}'.format(total_amount),
        'item_name': "Order-Item-Number-3",
        'invoice': "INVOICE_NO-3",
        'currency_code': "USD",
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('core:payment-completed')),
        'cancel_url': 'http://{}{}'.format(host, reverse('core:payment-failed')),
    }

    paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)

    return render(request, 'core/checkout.html', {
        'total_amount': total_amount,
        'paypal_payment_button': paypal_payment_button,
    })

def payment_completed_view(request):
    return render(request, 'core/payment-completed.html')

def payment_failed_view(request):
    return render(request, 'core/payment-failed.html')
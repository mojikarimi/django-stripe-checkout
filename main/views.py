from django.shortcuts import render, redirect  # new
from django.conf import settings  # new
from django.urls import reverse  # new
import stripe  # new


def index(request):  # new
    stripe.api_key = settings.STRIPE_SECRET_KEY
    price = 50
    price_dolor = price * 100
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    'unit_amount': price_dolor,
                },
                'quantity': 1,
            }],
            mode="payment",
            customer_creation='always',
            success_url=request.build_absolute_uri(reverse("success")),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )
        return redirect(checkout_session.url, code=303)
    return render(request, "index.html")


def success(request):
    return render(request, "success.html")


def cancel(request):
    return render(request, "cancel.html")

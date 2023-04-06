# app2/api/views.py
import stripe
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TicketSerializer
stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(["POST"])
def create_checkout_session(request):
    serializer = TicketSerializer(data=request.data)

    if serializer.is_valid():
        adults_tickets = serializer.validated_data["adults_tickets"]
        children_tickets = serializer.validated_data["children_tickets"]

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": 1000,
                        "product_data": {
                            "name": "Adult Ticket",
                        },
                    },
                    "quantity": adults_tickets,
                },
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": 500,
                        "product_data": {
                            "name": "Children Ticket",
                        },
                    },
                    "quantity": children_tickets,
                },
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/canceled",
        )

    return Response({"url": session.url})

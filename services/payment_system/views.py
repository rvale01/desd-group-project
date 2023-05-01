# app2/api/views.py
import stripe
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TicketSerializer

stripe.api_key = "sk_test_51ML6GvA5JuwZl2aDVTNJ2ITAXhbXiGWTJTKbvQVs0eDqnMOn9GTjOB46QGUgR3Ad2kZ664yHFI1OCG0sAneQZyln00n8Zu12I7"

@api_view(["POST"])
def create_default_checkout_session(request):
    serializer = TicketSerializer(data=request.data)

    if serializer.is_valid():
        adults_tickets = serializer.validated_data["adults_tickets"]
        children_tickets = serializer.validated_data["children_tickets"]

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "gbp",
                        "unit_amount": 1000,
                        "product_data": {
                            "name": "Adult Tickets",
                        },
                    },
                    "quantity": adults_tickets,
                },
                {
                    "price_data": {
                        "currency": "gbp",
                        "unit_amount": 500,
                        "product_data": {
                            "name": "Children Tickets",
                        },
                    },
                    "quantity": children_tickets,
                },
            ],
            mode="payment",
            success_url="http://example.com/success",
            cancel_url="http://example.com/canceled",
        )

    return Response({"url": session.url})

@api_view(["POST"])
def create_club_checkout_session(request):
    serializer = TicketSerializer(data=request.data)

    if serializer.is_valid():
        amount = serializer.validated_data["amount"]
        club_id = serializer.validated_data["club_id"]

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "gbp",
                        "unit_amount": int(amount),
                        "product_data": {
                            "name": "Payment for account n. " + club_id,
                        },
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="http://example.com/success",
            cancel_url="http://example.com/canceled",
        )

    return Response({"url": session.url})
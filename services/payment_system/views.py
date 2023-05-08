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

        line_items = [
            {
                "price_data": {
                    "currency": "gbp",
                    "unit_amount": 1000,
                    "product_data": {
                        "name": "Adult Tickets",
                    },
                },
                "quantity": adults_tickets,
            }
        ]

        if children_tickets >= 1:
            line_items.append(
                {
                    "price_data": {
                        "currency": "gbp",
                        "unit_amount": 700,
                        "product_data": {
                            "name": "Children Tickets",
                        },
                    },
                    "quantity": children_tickets,
                }
            )
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://localhost:8000/customer/success",
            cancel_url="http://localhost:8000",
        )

    return Response({"url": session.url})


@api_view(["POST"])
def add_credit(request):
    serializer = TicketSerializer(data=request.data)

    if serializer.is_valid():
        username = serializer.validated_data["username"]
        amount = int(serializer.validated_data["amount"])
        success_url = serializer.validated_data["success_url"]

        line_items = [
            {
                "price_data": {
                    "currency": "gbp",
                    "unit_amount": amount * 100,
                    "product_data": {
                        "name": "Top up for " + username,
                    },
                },
                "quantity": 1,
            }
        ]
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://localhost:8000/" + success_url,
            cancel_url="http://localhost:8000/",
        )

    return Response({"url": session.url})
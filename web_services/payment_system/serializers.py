# api/serializers.py
from rest_framework import serializers


class TicketSerializer(serializers.Serializer):
    adults_tickets = serializers.IntegerField(min_value=0)
    children_tickets = serializers.IntegerField(min_value=0)
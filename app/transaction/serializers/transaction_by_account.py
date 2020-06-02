
from rest_framework import serializers


class TransactionByAccountSerializer(serializers.Serializer):
    """Serializer for list summary by account"""
    account = serializers.CharField()
    balance = serializers.CharField()
    total_inflow = serializers.CharField()
    total_outflow = serializers.CharField()

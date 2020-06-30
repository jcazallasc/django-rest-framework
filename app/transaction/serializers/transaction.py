
from rest_framework import serializers

from core.models import Transaction
from transaction.constants.transaction import VALID_TYPES


class TransactionListSerializer(serializers.ListSerializer, list):
    def validate(self, items):
        reference_unique_list = list()
        validated_data = list()

        for item in items:
            if item['reference'] not in reference_unique_list:
                reference_unique_list.append(item['reference'])
                validated_data.append(item)

        return validated_data

    def create(self, validated_data):
        transactions = [Transaction(**item) for item in validated_data]
        return Transaction.objects.bulk_create(transactions)


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for transaction objects"""

    class Meta:
        model = Transaction
        list_serializer_class = TransactionListSerializer
        fields = ('reference', 'account', 'date', 'amount', 'type', 'category')

    def validate(self, data):
        self._validate_type(data.get('type'))
        self._validate_amount(data.get('type'), data.get('amount'))
        return data

    def _validate_type(self, type):
        if type not in VALID_TYPES.keys():
            msg = 'Type must be {}'.format(
                ', '.join(VALID_TYPES.keys())
            )
            raise serializers.ValidationError(msg)

    def _validate_amount(self, type, amount):
        type_amount_validator = VALID_TYPES.get(type).get('amount')
        operator = type_amount_validator.get('operator')
        value = type_amount_validator.get('value')

        if not operator(float(amount), value):
            raise serializers.ValidationError(
                type_amount_validator.get('error').format(value)
            )

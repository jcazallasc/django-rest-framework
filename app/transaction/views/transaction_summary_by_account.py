from typing import List

from rest_framework import generics
from rest_framework.response import Response

from core.models import Transaction
from core.views.base_auth import BaseAuthView
from helpers.transformers import convert_dict_values_inside_list
from transaction.serializers.transaction import TransactionSerializer


class TransactionSummaryByAccountView(BaseAuthView, generics.ListAPIView):
    """List transactions by account"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(
            user=self.request.user
        ).order_by('-reference')

    def transform_by_account(self, data) -> List[dict]:
        """Transform data incoming from serializer into desired structure"""
        result = {}
        for row in data:
            _amount = float(row['amount'])
            _account = row['account']
            _type = row['type']

            if _account not in result:
                result[_account] = {
                    'balance': float(0),
                    'total_inflow': float(0),
                    'total_outflow': float(0),
                }

            result[_account]['balance'] += _amount
            result[_account]['total_{}'.format(_type)] += _amount

        result = self._convert_to_output_structure(result)

        return convert_dict_values_inside_list(str, result)

    def _convert_to_output_structure(self, data: dict) -> List[dict]:
        return [
            {'account': account, **data}
            for account, data in data.items()
        ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(self.transform_by_account(serializer.data))

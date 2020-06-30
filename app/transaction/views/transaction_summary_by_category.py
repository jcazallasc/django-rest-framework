from rest_framework import generics
from rest_framework.response import Response

from core.models import Transaction
from core.views.base_auth import BaseAuthView
from helpers.transformers import convert_dict_values_inside_dict
from transaction.serializers.transaction import TransactionSerializer


class TransactionSummaryByCategoryView(BaseAuthView, generics.ListAPIView):
    """List transactions by category"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        queryset = self.queryset

        _from = self.request.query_params.get('from')
        if _from:
            queryset = queryset.filter(date__gte=_from)

        _to = self.request.query_params.get('to')
        if _to:
            queryset = queryset.filter(date__lte=_to)

        return queryset.filter(
            user=self.request.user
        ).order_by('-reference')

    def transform_by_category(self, data) -> dict:
        """Transform data incoming from serializer into desired structure"""
        result = {}
        for row in data:
            _amount = float(row['amount'])
            _type = row['type']
            _category = row['category']

            if _type not in result:
                result.update({_type: {}})

            if _category not in result[_type]:
                result[_type].update({_category: float(0)})

            result[_type][_category] += _amount

        return convert_dict_values_inside_dict(str, result)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(self.transform_by_category(serializer.data))

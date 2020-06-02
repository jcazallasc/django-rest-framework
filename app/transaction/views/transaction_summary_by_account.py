from decimal import Decimal

from django.db.models import Case, Sum, When
from rest_framework import generics

from core.models import Transaction
from core.views.base_auth import BaseAuthView
from transaction.serializers.transaction_by_account import \
    TransactionByAccountSerializer


class TransactionSummaryByAccountView(BaseAuthView, generics.ListAPIView):
    """List transactions by account"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionByAccountSerializer
    filterset_fields = ['date']

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        queryset = self.queryset

        _from = self.request.query_params.get('from')
        if _from:
            queryset = queryset.filter(date__gte=_from)

        _to = self.request.query_params.get('to')
        if _to:
            queryset = queryset.filter(date__lte=_to)

        return queryset\
            .filter(user=self.request.user)\
            .values('account')\
            .annotate(
                balance=Sum('amount'),
                total_inflow=Sum(
                    Case(
                        When(type='inflow', then='amount'),
                        When(type='outflow', then=Decimal('0.00')),
                    ),
                ),
                total_outflow=Sum(
                    Case(
                        When(type='outflow', then='amount'),
                        When(type='inflow', then=Decimal('0.00')),
                    ),
                ),
            )

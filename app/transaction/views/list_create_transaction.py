from rest_framework import generics

from core.models import Transaction
from core.views.base_auth import BaseAuthView
from transaction.serializers.transaction import TransactionSerializer


class ListCreateTransactionView(BaseAuthView, generics.ListCreateAPIView):
    """List/Create transactions"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_serializer(self, *args, **kwargs):
        """Allows bulk creation of a resource."""
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(
            user=self.request.user
        ).order_by('-reference')

    def perform_create(self, serializer):
        """Create a new transaction"""
        serializer.save(user=self.request.user)

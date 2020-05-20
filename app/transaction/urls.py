from django.urls import path

from transaction.views.list_create_transaction import ListCreateTransactionView
from transaction.views.transaction_summary_by_account import \
    TransactionSummaryByAccountView
from transaction.views.transaction_summary_by_category import \
    TransactionSummaryByCategoryView

app_name = 'transaction'

urlpatterns = [
    path('create/', ListCreateTransactionView.as_view(), name='create'),
    path('list/', ListCreateTransactionView.as_view(), name='list'),
    path(
        'summary-by-account/',
        TransactionSummaryByAccountView.as_view(),
        name='summary-account',
    ),
    path(
        'summary-by-category/',
        TransactionSummaryByCategoryView.as_view(),
        name='summary-category',
    ),
]

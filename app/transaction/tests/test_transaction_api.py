from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Transaction
from helpers.tests import sample_transaction, sample_user
from transaction.constants.transaction import TYPE_INFLOW, TYPE_OUTFLOW
from transaction.serializers.transaction import TransactionSerializer

TRANSACTION_CREATE_URL = reverse('transaction:create')
TRANSACTION_LIST_URL = reverse('transaction:list')
TRANSACTION_SUMMARY_BY_ACCOUNT = reverse('transaction:summary-account')
TRANSACTION_SUMMARY_BY_CATEGORY = reverse('transaction:summary-category')


class PublicTransactionApiTests(TestCase):
    """Test the available Transaction API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving Transactions"""
        res = self.client.get(TRANSACTION_LIST_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTransactionsApiTests(TestCase):
    """Test the authorized user transactions API"""

    def setUp(self):
        self.user = sample_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_transactions(self):
        """Test retrieving transactions"""
        sample_transaction(
            user=self.user,
            reference='00001',
        )
        sample_transaction(
            user=self.user,
            reference='00002',
        )

        res = self.client.get(TRANSACTION_LIST_URL)

        transactions = Transaction.objects.all().order_by('-reference')
        serializer = TransactionSerializer(transactions, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_transactions_limited_to_user(self):
        """Test that transactions returned are for the authenticated user"""
        user2 = sample_user(email='other@test.com')
        sample_transaction(user=user2, reference='user2')
        transaction = sample_transaction(user=self.user, reference='user')

        res = self.client.get(TRANSACTION_LIST_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['reference'], transaction.reference)

    def test_create_transaction_successful(self):
        """Test creating transaction"""
        payload = {
            'reference': '000009',
            'account': 'C0012',
            'date': '2020-12-12',
            'amount': '100',
            'type': TYPE_INFLOW,
            'category': 'category',
        }
        self.client.post(TRANSACTION_CREATE_URL, payload)

        exists = Transaction.objects.filter(
            reference='000009'
        ).exists()
        self.assertTrue(exists)

    def test_create_transaction_invalid(self):
        """Test creating a new invalid transaction"""
        payload = {
            'reference': '',
            'account': '',
            'date': '',
            'amount': '',
            'type': '',
            'category': '',
        }
        res = self.client.post(TRANSACTION_CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_transactions_successful(self):
        """Test that transaction list is returned"""
        sample_transaction(
            user=self.user,
            reference='000001',
        )
        sample_transaction(
            user=self.user,
            reference='000002',
        )

        res = self.client.get(TRANSACTION_LIST_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_summary_by_account(self):
        """Test that the summary by account view is returning the right data"""
        account1 = 'C00001'
        account2 = 'C00002'
        sample_transaction(
            user=self.user,
            reference='000001',
            account=account1,
            amount='1',
            type=TYPE_INFLOW,
        )
        sample_transaction(
            user=self.user,
            reference='000002',
            account=account1,
            amount='1',
            type=TYPE_OUTFLOW,
        )
        sample_transaction(
            user=self.user,
            reference='000003',
            account=account2,
            amount='1',
            type=TYPE_OUTFLOW,
        )

        res = self.client.get(TRANSACTION_SUMMARY_BY_ACCOUNT)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data[0]['account'], account1)
        self.assertEqual(res.data[0]['balance'], '2.00')
        self.assertEqual(res.data[0]['total_inflow'], '1.00')
        self.assertEqual(res.data[0]['total_outflow'], '1.00')
        self.assertEqual(res.data[1]['account'], account2)
        self.assertEqual(res.data[1]['balance'], '1.00')
        self.assertEqual(res.data[1]['total_inflow'], '0.00')
        self.assertEqual(res.data[1]['total_outflow'], '1.00')

    def test_summary_by_category(self):
        """
        Test that the summary by category view is returning the right data
        """
        category1 = 'category1'
        category2 = 'category2'
        sample_transaction(
            user=self.user,
            reference='000001',
            amount='1',
            type=TYPE_INFLOW,
            category=category1,
        )
        sample_transaction(
            user=self.user,
            reference='000002',
            amount='1',
            type=TYPE_OUTFLOW,
            category=category1,
        )
        sample_transaction(
            user=self.user,
            reference='000003',
            amount='1',
            type=TYPE_OUTFLOW,
            category=category2,
        )

        res = self.client.get(TRANSACTION_SUMMARY_BY_CATEGORY)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data[TYPE_OUTFLOW][category1], str(float(1)))
        self.assertEqual(res.data[TYPE_OUTFLOW][category2], str(float(1)))
        self.assertEqual(res.data[TYPE_INFLOW][category1], str(float(1)))
        self.assertNotIn(category2, res.data[TYPE_INFLOW])

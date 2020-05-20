from django.contrib.auth import get_user_model

from core.models import Transaction
from transaction.constants.transaction import TYPE_OUTFLOW


def sample_user(
    email='jcazallasc@gmail.com',
    password='password',
    name='Javier',
    age=30
):
    return get_user_model().objects.create_user(
        email=email,
        password=password,
        name=name,
        age=age,
    )


def sample_transaction(
    user,
    reference='000051',
    account='S00099',
    date='2020-01-13',
    amount='-51.13',
    type=TYPE_OUTFLOW,
    category='groceries',
):
    return Transaction.objects.create(
        user=user,
        reference=reference,
        account=account,
        date=date,
        amount=amount,
        type=type,
        category=category,
    )

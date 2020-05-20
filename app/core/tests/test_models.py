from django.contrib.auth import get_user_model
from django.test import TestCase

from helpers.tests import sample_transaction, sample_user


class Test(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email successful"""
        email = 'jcazallasc@gmail.com'
        user = sample_user(email=email)

        self.assertEqual(user.email, email)

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = 'jcazallasc@GMAIL.COM'
        user = sample_user(email=email)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            sample_user(email=None)

    def test_new_user_invalid_name(self):
        """Test creating user with no name raises error"""
        with self.assertRaises(ValueError):
            sample_user(name=None)

    def test_new_user_invalid_age(self):
        """Test creating user with no age raises error"""
        with self.assertRaises(ValueError):
            sample_user(age=0)

    def test_create_new_superuser(self):
        """Test creating a new superuse"""
        user = get_user_model().objects.create_superuser(
            email='jcazallasc@gmail.com',
            password='password',
            name='Javier',
            age=30,
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_transaction(self):
        """Test creating a new transaction"""
        reference = '000051'
        transaction = sample_transaction(
            user=sample_user(),
            reference=reference
        )

        self.assertEqual(reference, transaction.reference)

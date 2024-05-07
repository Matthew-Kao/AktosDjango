from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Account, Consumer
from django.core.management import call_command

class BaseTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('import_accounts', 'consumers_balances.csv')

class AccountEndpointTests(BaseTest):

    def test_no_params(self):
        response = self.client.get(reverse('accounts-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data['results']) > 0, "Should return some accounts")

    def test_min_balance_only(self):
        response = self.client.get(reverse('accounts-list') + '?min_balance=100')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertGreaterEqual(float(account['balance']), 100)

    def test_max_balance_only(self):
        response = self.client.get(reverse('accounts-list') + '?max_balance=5000000')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertLessEqual(float(account['balance']), 5000000)

    def test_consumer_name_only(self):
        response = self.client.get(reverse('accounts-list') + '?consumer_name=Jessica Williams')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertIn('Jessica Williams', account['consumer']['name'])

    def test_status_only(self):
        response = self.client.get(reverse('accounts-list') + '?status=active')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertEqual('active', account['status'])

    def test_min_and_max_balance(self):
        response = self.client.get(reverse('accounts-list') + '?min_balance=100&max_balance=5000000')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertTrue(100 <= float(account['balance']) <= 5000000)

    def test_min_balance_and_consumer_name(self):
        response = self.client.get(reverse('accounts-list') + '?min_balance=100&consumer_name=Jessica Williams')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertGreaterEqual(float(account['balance']), 100)
            self.assertIn('Jessica Williams', account['consumer']['name'])

    def test_min_balance_and_status(self):
        response = self.client.get(reverse('accounts-list') + '?min_balance=100&status=active')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertGreaterEqual(float(account['balance']), 100)
            self.assertEqual('active', account['status'])

    def test_max_balance_and_consumer_name(self):
        response = self.client.get(reverse('accounts-list') + '?max_balance=5000000&consumer_name=Jessica Williams')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertLessEqual(float(account['balance']), 5000000)
            self.assertIn('Jessica Williams', account['consumer']['name'])

    def test_max_balance_and_status(self):
        response = self.client.get(reverse('accounts-list') + '?max_balance=5000000&status=active')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertLessEqual(float(account['balance']), 5000000)
            self.assertEqual('active', account['status'])

    def test_consumer_name_and_status(self):
        response = self.client.get(reverse('accounts-list') + '?consumer_name=Jessica Williams&status=active')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertIn('Jessica Williams', account['consumer']['name'])
            self.assertEqual('active', account['status'])

    def test_min_max_balance_and_consumer_name(self):
        response = self.client.get(reverse('accounts-list') + '?min_balance=100&max_balance=5000000&consumer_name=Jessica Williams')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertTrue(100 <= float(account['balance']) <= 5000000)
            self.assertIn('Jessica Williams', account['consumer']['name'])

    def test_min_max_balance_and_status(self):
        response = self.client.get(reverse('accounts-list') + '?min_balance=100&max_balance=5000000&status=active')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertTrue(100 <= float(account['balance']) <= 5000000)
            self.assertEqual('active', account['status'])

    def test_min_balance_consumer_name_and_status(self):
        response = self.client.get(reverse('accounts-list') + '?min_balance=100&consumer_name=Jessica Williams&status=active')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertGreaterEqual(float(account['balance']), 100)
            self.assertIn('Jessica Williams', account['consumer']['name'])
            self.assertEqual('active', account['status'])

    def test_max_balance_consumer_name_and_status(self):
        response = self.client.get(reverse('accounts-list') + '?max_balance=5000000&consumer_name=Jessica Williams&status=active')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertLessEqual(float(account['balance']), 5000000)
            self.assertIn('Jessica Williams', account['consumer']['name'])
            self.assertEqual('active', account['status'])

    def test_all_params(self):
        response = self.client.get(reverse('accounts-list') + '?min_balance=100&max_balance=5000000&consumer_name=Jessica Williams&status=active')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data['results']:
            self.assertTrue(100 <= float(account['balance']) <= 5000000)
            self.assertIn('Jessica Williams', account['consumer']['name'])
            self.assertEqual('active', account['status'])
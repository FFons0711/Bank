import unittest
from main import Client


class ClientTests(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Client("Charlotte", "Rodriguez", "1249760221641717", 60297.78, 669)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(500), 60797.78, "Incorrect balance")

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(200), 60097.78, "Incorrect balance")
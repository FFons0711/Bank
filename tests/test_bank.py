import unittest
import pytest
from main import Client, validate_card, generate_number, compound_interest
from tickets.tickets import give_ticket


class ClientTests(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Client("Charlotte", "Rodriguez", "1249760221641717", 60297.78, 669)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(500), 60797.78, "Incorrect balance")

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(200), 60097.78, "Incorrect balance")
        
    def test_withdraw_insuficient_valance(self):    
        with self.assertRaises(NameError):
            self.account.withdraw(80000)


def test_validate_card():
    assert validate_card("1249760291234567") == True
    assert validate_card("1234567891234567") == False
    assert validate_card("12497602912345678") == False
    assert validate_card("12497602912345") == False
    assert validate_card("12497602cat") == False
    assert validate_card("cat") == False


def test_generate_number():
    number = generate_number("../data/database.csv")
    assert len(number) == 16


def test_compound_interest():
    n, y1, y2 = compound_interest(1000, 0.1, 4, 10)
    assert n == 2685.06
    assert y1 == [1103.81, 1218.4, 1344.89, 1484.51, 1638.62, 1808.73, 1996.5, 2203.76, 2432.54, 2685.06]
    assert y2 == [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0]


def test_give_ticket():
    n = give_ticket()
    for i in range(1, 20):
        assert next(n) == i
    with pytest.raises(StopIteration):
        next(n)

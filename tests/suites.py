import unittest
import main
from test_class import ClientTests


def bank_suite():
    suite = unittest.TestSuite()
    suite.addTest(ClientTests("test_deposit"))
    suite.addTest(ClientTests("test_withdraw"))
    suite.addTest(ClientTests("test_withdraw_insuficient_valance"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_suite())
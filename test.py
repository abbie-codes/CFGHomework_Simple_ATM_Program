from unittest import mock
from unittest import TestCase, main
from .main import pin_validated, withdrawal_validated, pin_length, positive_withdrawal_balance, check_pin_is_number

class TestPinValidated(TestCase):
    def testCorrectPin(self):
        expected = True
        result = pin_validated(2468)
        self.assertEqual(expected, result)

class TestPinLength(TestCase):
    def testPinLength(self):
        expected = True
        result = pin_length(2468)
        self.assertEqual(expected, result)

class TestWithdrawalValidated(TestCase):
    def testCorrectAmount(self):
        expected = True
        result = withdrawal_validated(90.00)
        self.assertEqual(expected, result)

class TestPositiveWithdrawalBalance(TestCase):
    def testAmountPositive(self):
        expected = True
        result = positive_withdrawal_balance(0.01)
        self.assertEqual(expected, result)

class TestPinIsNumber(TestCase):
    def testPinInt(self):
        expected = True
        result = check_pin_is_number(2468)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()

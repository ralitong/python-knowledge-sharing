import unittest
from unittest.mock import MagicMock, patch
from restaurant import Waiter, Chef

class RestaurantUnitTest(unittest.TestCase):
    """
    This class contains unit tests for the Restaurant application.
    """

    def setUp(self):
        self.waiter = Waiter()
        self.chef = Chef("John")


    def test_get_order_from_real_waiter_fails(self):
        """
        This test asserts that the order will not be Spaghetti since
        the waiter returns a random order.
        """
        order = self.waiter.getOrder()
        self.assertNotEqual(order, "Spaghetti")

    def test_get_order_from_magic_mocked_waiter(self):
        """
        This test asserts that the order will be Spaghetti since
        the waiter is mocked to return Spaghetti.
        """
        self.waiter = MagicMock(Waiter)
        self.waiter.getOrder.return_value = "Spaghetti"
        self.assertEqual(self.waiter.getOrder(), "Spaghetti")


    def test_get_order_from_patched_waiter(self):
        """
        This type of patching is useful when you want to mock a
        library function or a function from a third-party library.
        """
        with unittest.mock.patch('restaurant.Waiter.getOrder') as mocked_get_order:
            mocked_get_order.return_value = "Spaghetti"
            self.assertEqual(self.waiter.getOrder(), "Spaghetti")


    @patch('restaurant.Waiter.getOrder')
    def test_get_order_from_patched_waiter_using_a_decorator(self, mocked_get_order):
        """
        This is the same as the previous test except that we use
        the @patch decorator to patch the waiter.

        Note that you have to pass the mocked waiter as an argument
        to the test method.
        """
        mocked_get_order.return_value = "Spaghetti"
        self.assertEqual(self.waiter.getOrder(), "Spaghetti")




if __name__ == "__main__":
    unittest.main()

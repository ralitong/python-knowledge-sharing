import unittest
from unittest.mock import patch
from restaurant import Waiter

class RestaurantPatchSetupTeardownTest(unittest.TestCase):
    """
    This class contains patching during setUp and tearDown.
    """

    def setUp(self):
        self.waiter = Waiter()
        self.get_order_patcher = patch('restaurant.Waiter.getOrder').start()
        self.get_order_patcher.return_value = "Spaghetti"

    def tearDown(self):
        self.get_order_patcher.stop()
        # Alternatively, you can use the following to stop all patches:
        patch.stopall()

    def test_get_order_from_patched_waiter(self):
        """
        This test asserts that the order will be Spaghetti since
        the waiter is mocked to return Spaghetti.
        """
        self.assertEqual(self.waiter.getOrder(), "Spaghetti")

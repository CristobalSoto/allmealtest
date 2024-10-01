from django.test import TestCase
from menu.models import Menu, Order
from datetime import date

class OrderTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            date=date.today(),
            starter="Salad",
            main_course="Steak",
            dessert="Ice Cream"
        )
    
    def test_order_creation(self):
        """Test that an order is placed successfully."""
        order = Order.objects.create(
            user_id="U123456",
            menu=self.menu,
            selection="main_course"
        )
        self.assertEqual(order.selection, "main_course")
        self.assertEqual(order.user_id, "U123456")
        self.assertEqual(order.menu, self.menu)

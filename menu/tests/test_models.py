from django.test import TestCase
from menu.models import Menu
from datetime import date

class MenuModelTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            date=date.today(),
            starter="Salad",
            main_course="Steak",
            dessert="Ice Cream"
        )

    def test_menu_creation(self):
        """Test that a menu is created successfully."""
        self.assertEqual(self.menu.starter, "Salad")
        self.assertEqual(self.menu.main_course, "Steak")
        self.assertEqual(self.menu.dessert, "Ice Cream")
        self.assertEqual(self.menu.date, date.today())

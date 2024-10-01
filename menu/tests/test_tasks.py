# menu/tests/test_tasks.py

from django.test import TestCase
from celery.result import EagerResult
from menu.tasks import send_daily_menu
from menu.models import Menu
from datetime import date

class CeleryTasksTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            date=date.today(),
            starter="Salad",
            main_course="Steak",
            dessert="Ice Cream"
        )

    def test_send_daily_menu_task(self):
        """Test that the send_daily_menu task runs successfully."""
        result = send_daily_menu.apply()

        self.assertEqual(result.status, 'SUCCESS')
        self.assertIsInstance(result, EagerResult)

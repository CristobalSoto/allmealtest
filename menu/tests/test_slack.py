# menu/tests/test_slack.py

import json
from unittest.mock import patch
from django.test import TestCase
from menu.slack import send_menu_to_slack
from menu.models import Menu
from datetime import date

class SlackTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            date=date.today(),
            starter="Salad",
            main_course="Steak",
            dessert="Ice Cream"
        )

    @patch('menu.slack.requests.post')
    def test_send_menu_to_slack(self, mock_post):
        """Test that a Slack message is sent successfully."""
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'ok': True}  # Mock the JSON response

        response = send_menu_to_slack(self.menu, '#general')

        mock_post.assert_called_once()
        self.assertEqual(response['ok'], True)  # Now this will compare against the mocked response

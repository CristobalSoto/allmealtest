from celery import shared_task
from .slack import get_slack_users, send_menu_to_slack, send_reminder
from .models import Menu, Order
from datetime import date

@shared_task
def send_order_reminders():
    today_menu = Menu.objects.get(date=date.today())

    # Get all users in Slack
    slack_users = get_slack_users()
    
    # Get Slack user IDs who have placed an order
    users_with_orders = Order.objects.filter(menu=today_menu).values_list('user_id', flat=True)

    # Find users who haven't placed orders
    for user in slack_users:
        if not user['id'] in users_with_orders:
            send_reminder(user['id'])

@shared_task
def send_daily_menu():
    try:
        today_menu = Menu.objects.get(date=date.today())
        send_menu_to_slack(today_menu, '#general')  # Replace '#general' with your channel ID or name
        print(f"Menu for {date.today()} sent successfully!")
    except Menu.DoesNotExist:
        print(f"No menu found for {date.today()}")
import requests
from django.conf import settings

def send_menu_to_slack(menu, channel):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {settings.SLACK_BOT_TOKEN}'
    }
    
    data = {
        'channel': channel,
        'blocks': [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Today's menu:\n\n*Starter:* {menu.starter}\n*Main Course:* {menu.main_course}\n*Dessert:* {menu.dessert}"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": menu.starter},
                        "value": "starter",
                        "action_id": "choose_starter"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": menu.main_course},
                        "value": "main_course",
                        "action_id": "choose_main_course"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": menu.dessert},
                        "value": "dessert",
                        "action_id": "choose_dessert"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"Failed to send message to Slack: {response.text}")
    
    return response.json()

def send_reminder(user_id):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {settings.SLACK_BOT_TOKEN}'
    }
    
    data = {
        'channel': user_id,  # Send the message directly to the user
        'text': "Hey! Don't forget to place your order for today's meal.",
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"Failed to send reminder: {response.text}")
    
    return response.json()

def send_confirmation(user, selection):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {settings.SLACK_BOT_TOKEN}'
    }
    
    data = {
        'channel': user,
        'text': f"Thank you! Your order for {selection} has been received.",
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"Failed to send confirmation message: {response.text}")
    
    return response.json()

def get_slack_users():
    url = 'https://slack.com/api/users.list'
    headers = {
        'Authorization': f'Bearer {settings.SLACK_BOT_TOKEN}'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch Slack users: {response.text}")
    
    users = response.json()['members']
    return users
from datetime import date, datetime, time
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .slack import send_confirmation, send_menu_to_slack
from .models import Menu, Order
from .serializers import MenuSerializer
import json
from django.views.decorators.csrf import csrf_exempt

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @action(detail=False, methods=['post'])
    def send_menu(self, request):
        try:
            # For simplicity, we'll assume there is only one menu for today
            from datetime import date
            today_menu = Menu.objects.get(date=date.today())
            
            # Send the menu to Slack
            send_menu_to_slack(today_menu, '#general')  # Adjust Slack channel here
            
            return Response({'status': 'Menu sent to Slack successfully!'})
        except Menu.DoesNotExist:
            return Response({'error': 'No menu found for today.'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

@csrf_exempt
def slack_interact(request):
    if request.method == 'POST':
        # Check if the current time is between 12:00 and 12:30
        now = datetime.now().time()
        order_start = time(12, 0)
        order_end = time(12, 30)

        if not (order_start <= now <= order_end):
            return JsonResponse({'error': 'Ordering time has passed!'}, status=403)

        payload = json.loads(request.POST['payload'])
        
        if payload['type'] == 'block_actions':
            action = payload['actions'][0]
            user = payload['user']['id']
            selected_option = action['value']
            today_menu = Menu.objects.get(date=date.today())

            # Store the user's selection as an order in the database
            order = Order.objects.create(
                user_id=user,
                menu=today_menu,
                selection=selected_option
            )
            
            return JsonResponse({'ok': True, 'message': 'Order saved successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def home(request):
    return HttpResponse("<h1>Welcome to the AllMeal API</h1><p>Use /api/menus/ to manage menus.</p>")
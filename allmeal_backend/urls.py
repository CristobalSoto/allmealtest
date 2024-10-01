from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu.views import MenuViewSet, home, slack_interact

router = DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menu')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/menus/send_menu/', MenuViewSet.as_view({'post': 'send_menu'})),
    path('api/slack/interact/', slack_interact), 
    path('', home),  # Add this line to route the root URL
]
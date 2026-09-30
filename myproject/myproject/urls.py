"""
URL configuration for myproject project.
"""
from django.contrib import admin
from django.urls import path
# අපි core app එකේ views ගෙන්නගන්නවා
from core.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # මුල් පිටුවට (Home page) යනකොට අපේ home_view එක ක්‍රියාත්මක වෙන්න දානවා
    path('', home_view, name='home'),
]
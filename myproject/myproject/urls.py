from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # Django හි authentication views ගෙන්වා ගැනීම
from core.views import home_view, add_topic_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('add/', add_topic_view, name='add_topic'),
    path('signup/', signup_view, name='signup'),
    
    # Login සහ Logout සඳහා බිල්ට්-ඉන් views භාවිතය
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
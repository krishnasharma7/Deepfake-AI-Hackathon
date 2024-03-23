from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "users"
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
]
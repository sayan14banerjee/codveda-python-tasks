from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('password-reset/', views.password_reset_request_view, name='password_reset'),
    path('password-reset-verify/', views.password_reset_verify_view, name='password_reset_verify'),
]

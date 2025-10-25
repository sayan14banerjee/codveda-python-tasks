from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
import random

# Register
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    return render(request, 'accounts/register.html')


# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'accounts/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')   # redirect to login page if not logged in
def home_view(request):
    return render(request, 'accounts/home.html')
# Password Reset (via email OTP)
otp_storage = {}

def password_reset_request_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            otp = str(random.randint(100000, 999999))
            otp_storage[email] = otp
            try:
                send_mail(
                    'Password Reset OTP',
                    f'Your OTP is: {otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'OTP sent to your email.')
                return redirect('password_reset_verify')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
        else:
            messages.error(request, "Email not found.")
    return render(request, 'accounts/password_reset_request.html')


def password_reset_verify_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_password = request.POST.get('new_password')

        # Check if OTP is valid
        if otp_storage.get(email) == otp:
            users = User.objects.filter(email=email)
            if users.exists():
                for user in users:  # handle multiple users with same email
                    user.set_password(new_password)
                    user.save()

                otp_storage.pop(email)
                messages.success(request, "Password reset successful for all accounts with this email.")
                return redirect('login')
            else:
                messages.error(request, "No user found with this email.")
        else:
            messages.error(request, "Invalid OTP or Email.")
    return render(request, 'accounts/password_reset_confirm.html')


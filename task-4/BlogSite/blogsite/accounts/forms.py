from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label='Enter your registered email')

class SetNewPasswordForm(forms.Form):
    otp = forms.CharField(label='OTP')
    new_password = forms.CharField(widget=forms.PasswordInput, label='New Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

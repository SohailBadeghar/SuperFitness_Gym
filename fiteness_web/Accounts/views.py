from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from Accounts.forms import RegistrationForm
from .mail import send_account_activation_email
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import View
import time
import uuid


class RegisterForm(View):

    def post(self, request):
        if not request.user.is_authenticated:
            fm = RegistrationForm(request.POST)
            password = request.POST.get('password')
            if fm.is_valid():
                user = fm.save()
                user.set_password(password)
                user.save()
                messages.success(
                    request, 'your account has been signed up successfully!')
                time.sleep(10)
                return redirect('login')
        else:
            return HttpResponseRedirect('/')

    def get(self, request):
        fm = RegistrationForm()
        return render(request, 'Accounts/registration.html', {'forms': fm})


class LoginForm(View):
    def post(self, request):
        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']

            print(username, password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials')

    def get(self, request):
        return render(request, 'Accounts/login.html')


# <-------------------------------------------ForgetPassword View Function-------------------------------------->

class ForgetPassword(View):
        def post(self, request):
            try:
                username = request.POST.get('username')
                if not CustomUser.objects.filter(email=username).first():
                    messages.success(
                        request, 'Not User found with this username.')
                    return redirect('/Forget_Password/')
                user_obj = CustomUser.objects.get(email=username)
                token = str(uuid.uuid4())
                # send_account_activation_email(user_obj, token)
                messages.success(request, ' An Email is Sent.')
                return render(request, 'Accounts/Reset_conf.html')
            except Exception as e:
                print(e)

        def get(self, request):
            return render(request, 'Accounts/forget_password.html')


# <----------------------------- reset template message page ----------------------------->

class reset_template(View):
    def get(self, request):
        return render(request, 'Accounts/Reset_conf.html')
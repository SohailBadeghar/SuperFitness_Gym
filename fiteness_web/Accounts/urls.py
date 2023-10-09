from django.urls import path
from .views import *
urlpatterns = [
    path('registration/',RegisterForm.as_view(), name="registration"), # type: ignore
    path('login/',LoginForm.as_view(), name="login"),
    path('forget_Password/',ForgetPassword.as_view(),name='forget_Password'),
    path('reset/',reset_template.as_view(),name='reset'),

]
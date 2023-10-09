from django.urls import path
from .views import dj
urlpatterns = [
    path('home/', dj , name="home")
]
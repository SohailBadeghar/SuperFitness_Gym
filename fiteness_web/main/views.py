from django.shortcuts import render

def dj(request):
    return render(request,'main/home.html')
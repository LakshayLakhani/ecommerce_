from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def all_users(request):
    user = User.objects.all()

    return render(request, "all_users.html",{"user":user})

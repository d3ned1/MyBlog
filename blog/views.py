from django.shortcuts import render

from django.http import HttpResponse
from blog import models


def base(request):
    return render(request, 'blog/base.html')


def home(request):
    return render(request, 'blog/home.html')
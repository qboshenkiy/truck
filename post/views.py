from django.shortcuts import render
from .models import addNews

# Create your views here.
def index(req):
    return render(req, 'index.html', context={'posts': addNews.objects.all()})
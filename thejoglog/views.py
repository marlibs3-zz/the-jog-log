from django.shortcuts import render
from .models import Log


def home(request):
    logs = Log.objects.all()
    return render(request, 'home.html', {'logs': logs})

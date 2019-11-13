from django.shortcuts import render, redirect
from .models import Log


def home(request):
    logs = Log.objects.all().order_by('date')
    return render(request, 'home.html', {'logs': logs})


def new_log(request):
    if request.method == 'POST':
        date = request.POST['date']
        distance = request.POST['distance']
        time = request.POST['time']
        weight = request.POST['weight']

        Log.objects.create(
            date=date,
            distance=distance,
            time=time,
            weight=weight,
        )

        return redirect('home')

    return render(request, 'new_log.html')

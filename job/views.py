from django.shortcuts import render
from datetime import datetime 


def home(request):
    date_time = '1000'
    name_test = 'Парампампам'
    d = {'date_time': date_time, 'name_test': name_test}
    return render(request, 'home.html', d)
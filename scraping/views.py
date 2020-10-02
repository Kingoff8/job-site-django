from django.shortcuts import render
from .models import Vacancy

def home_view(request):
    sq = Vacancy.objects.all()
    return render(request, 'scraping/home.html', {'object_list': sq})

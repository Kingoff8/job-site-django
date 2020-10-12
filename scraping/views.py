from django.shortcuts import render
from .models import Vacancy

def home_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    
    #if city or language:
        

    sq = Vacancy.objects.all()
    return render(request, 'scraping/home.html', {'object_list': sq})

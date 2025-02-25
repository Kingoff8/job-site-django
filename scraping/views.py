from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm

def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    experience = request.GET.get('experience')
    qs = []
    
    if city or language or experience:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        if experience:
            _filter['experience__slug'] = experience

        
        qs  = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': qs,
    'form': form})

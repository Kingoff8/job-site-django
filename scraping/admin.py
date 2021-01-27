from django.contrib import admin
from .models import City, Language, Vacancy, Experience

admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
admin.site.register(Experience)
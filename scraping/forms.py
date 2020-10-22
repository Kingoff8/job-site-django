from django import forms
from scraping.models import City, Language, Vacancy

#class FindForm(forms.Form):
    #city =forms.ModelChoiceField(queryset=City.objects.all()) # добавлена одна скобка, после раскоммент удалить
    # , to_field_name='slug',
    # required=False, 
    # widget=forms.Select(attrs={'class': 'form-control mr-sm-2'}),
    # label='Город')
    
    #language =forms.ModelChoiceField(queryset=Language.objects.all()) # добавлена одна скобка, после раскоммент удалить
    # , to_field_name='slug',
    # required=False,
    # widget=forms.Select(attrs={'class': 'form-control custom-select mr-sm-2'}),
    # label='Специальность')

class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name="slug", required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Город'
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), to_field_name="slug", required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Специальность'
        )
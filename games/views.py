from django.shortcuts import render
from django.views.generic import DetailView

from .models import Hra, Vyvojar, Kategorie

# Create your views here.

def index(request):
    context = {
        'nadpis': 'Hry',
        'hry': Hra.objects.all(),
        'vyvojari': Vyvojar.objects.all(),
        'kategorie': Kategorie.objects.order_by('nazevKategorie')
    }
    return render(request, 'index.html', context=context)

class HraDetailView(DetailView):
    model = Hra
    template_name = 'game/detail.html'
    context_object_name = 'hra'

class VyvojarDetailView(DetailView):
    model = Vyvojar
    template_name = 'developer/detail.html'
    context_object_name = 'vyvojar'

def category_detail(request, pk):
    context = {
        'categories': Kategorie.objects.all(),
        'kategorie': Kategorie.objects.get(pk=pk),
        'hry': Hra.objects.filter(kategorie=pk)
    }
    return render(request, 'category/detail.html', context=context)
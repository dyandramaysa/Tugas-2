from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'nama' : 'Nadira Maysa Dyandra',
        'NPM' : '2106632232',
        'katalog' : data_item_katalog,
        }
    return render(request, 'katalog.html', context)
from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    return render(request, "watchlist.html",)

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data_watchlist = WatchList.objects.all()
    context = {
        'list_tontonan': data_watchlist,
        'nama': 'Nadira Maysa Dyandra',
        'NPM': '2106632232',
        }
    return render(request, "watchlist.html", context)
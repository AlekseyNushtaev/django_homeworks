import csv

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        res = []
        for row in reader:
            res.append(row)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(res, 10)
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)

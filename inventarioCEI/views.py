from time import strftime

from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def calendar(request):
    # fechas de prestamos se guardan f = datetime.datetime(2018, 5, 7, 15, 0, tzinfo=<UTC>) año mes día hora y min en utc
    # f.year =2018
    # d = date.today()
    # d.weekday() = 0 -> lunes
    today = date.today()
    day = today.day
    weekday = today.weekday()
    week = []

    for i in range(day - weekday, day - weekday + 7):
        week.append(i)

    weekStart = today.replace(day = day-weekday)
    weekEnd = today.replace(day = day + 6 - weekday)

    month = [weekStart, weekEnd]

    prestamos = Prestamo.objects.filter(fh_ini_prestamo__range=[weekStart, weekEnd]) | Prestamo.objects.filter(fh_fin_prestamo__range=[weekStart, weekEnd])

    return render(request, 'inventarioCEI/calendario.html', {'week': week, 'month': month, 'prestamos': prestamos})


def buscar(request):
    if request.method == "POST":
        busqueda = request.POST['elemento']
        lista = Articulo.objects.filter(lista_tags__contains=busqueda)
        return render(request, 'inventarioCEI/buscar.html', {'lista': lista})
    else:
        lista = []
        return render(request, 'inventarioCEI/buscar.html', {'lista': lista})


class LandingAdmin(TemplateView):
    template_name = "inventarioCEI/landingPageAdmin.html"

    def get_context_data(self, **kwargs):
        return {}

        # para hacer calendario: tomar semana actual, ver de la lista de prestamos, cuales corresponden a la semana actual, darselos al hrml, este revisa cada grilla y ve si corresponde a la hora,

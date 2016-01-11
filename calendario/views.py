from django.shortcuts import render
from django.http import HttpResponse
from .models import Partido, Jornada
from ligapp.models import Equipo, Jugador
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.

def calendario(request):
	jornadas=Jornada.objects.order_by('numero')
	contexto={"jornadas":jornadas}
	return render(request,"calendario.html",contexto)
	
def mostrarJornada(request, jornadaNum):
	jornada=Jornada.objects.get(numero__iexact=jornadaNum)
	partidos=Partido.objects.filter(jornada=jornada)
	partidos=partidos.order_by('fechaInicio')
	contexto={"jornada":jornada, "partidos":partidos}
	return render(request,"jornada.html",contexto)

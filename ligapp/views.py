from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Equipo, Jugador
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render,render_to_response, redirect
from .forms import *

# Create your views here.

def clasificacion(request):
	equipos=Equipo.objects.order_by('-puntos')
	contexto={"equipos":equipos}
	return render(request,"clasificacion.html",contexto)
	
def mostrarEquipo(request, nomEquipo):
	equipo=Equipo.objects.get(nombreUrl__iexact=nomEquipo)
	jugadores=Jugador.objects.filter(equipo=equipo)
	jugadores=jugadores.order_by('dorsal')
	contexto={"equipo":equipo, "jugadores":jugadores}
	return render(request,"equipo.html",contexto)
	
def crearEquipo(request):
	equipo=Equipo()
	if request.method=="POST":
		formulario=EquipoForm(request.POST,request.FILES,instance=equipo)
		if formulario.is_valid():
			formulario.save()
			return redirect('/')
	else:
		formulario=EquipoForm()
	context={'formulario':formulario}
	return render(request,"crear.html",context)
	
def modEquipo(request, nombreEquipo):
	equipo=Equipo.objects.get(nombreUrl__iexact=nombreEquipo)
	if request.method=="POST":
		formulario=EquipoForm(request.POST,request.FILES,instance=equipo)
		if formulario.is_valid():
			formulario.save()
			return redirect('/')
	else:
		formulario=EquipoForm(instance=equipo)
	context={'formulario':formulario, 'equipo':equipo}
	return render(request,"modificar.html",context)

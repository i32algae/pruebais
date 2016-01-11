from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.

def menuPrincipal(request):
	return render(request,"menuPrincipal.html")

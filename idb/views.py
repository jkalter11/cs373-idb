from django.shortcuts import *
from django.template import RequestContext

def home(request):
	return render_to_response('home.html', {}, RequestContext(request))

# Create your views here.

def metroid(request):
	return render_to_response('metroid.html', {}, RequestContext(request))

def yoshio_sakamoto(request):
	return render_to_response('yoshio_sakamoto.html', {}, RequestContext(request))

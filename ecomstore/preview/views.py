# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
#def home(request):
#	return render_to_response("index_test.html")

def home(request):
	return render_to_response("index.html",locals(),context_instance=RequestContext(request))

def contact(request):
	return render_to_response("contact.html",locals(),context_instance=RequestContext(request))

def about(request):
	return render_to_response("about.html",locals(),context_instance=RequestContext(request))

def services(request):
	return render_to_response("services_bs.html",locals(),context_instance=RequestContext(request))

def shop_online(request):
	return render_to_response("shop_online.html",locals(),context_instance=RequestContext(request))


# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    hola = 'hola como estai'
    return render_to_response('home.html',RequestContext(request,{'hola': hola}));


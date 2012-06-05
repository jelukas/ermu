# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from models import Erm
from forms import ErmForm

@login_required
def home(request):
    erm_list = Erm.objects.all()
    return render_to_response('home.html',RequestContext(request,{'erm_list': erm_list}))

@login_required
def nuevo(request):
    ermform = ErmForm()
    if request.method == 'POST':
        ermform = ErmForm(request.POST, request.FILES)
        if ermform.is_valid():
            ermform.save()
            #do something.
    return render_to_response('new_erm.html',RequestContext(request,{'ermform' : ermform}))

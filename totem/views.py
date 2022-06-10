from pdb import post_mortem

from django.shortcuts import render
from django.template import context

from totem.forms import TotemForm
from totem.models import Totem

# Create your views here.


def index_totem(request):
    if request.method =="POST":
        forms = TotemForm(request.POST)
        if forms.is_valid():
            forms.save()
    
    pacientes = Totem.objects.all()
    dados = {
        "pacientes":pacientes
    }
    return render(request,"index.html", context=pacientes)
            
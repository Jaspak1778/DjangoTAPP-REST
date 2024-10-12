from django.shortcuts import render 
from tietokanta.models import Events

def home(request):
    tapahtumat = Events.objects.all()
    context = {'tapahtumia': tapahtumat}
    return render(request, 'index.html',context)
from django.shortcuts import render
from .models import Block_de_espuma
from django.http import HttpResponse
from datetime import date
from datetime import time 
from datetime import timedelta
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('invapp.view_block_de_espuma')
def index(request):
    today = date.today()
    if request.GET.get('hoy'):
        blocks = Block_de_espuma.objects.filter(creado__day= today.day)
        # blocks = Block_de_espuma.objects.filter(creado__range=["2011-01-01", "2011-01-31"])
    else:
        if request.GET.get('semana'):
            inicio_de_semana = today - timedelta(days=today.weekday())
            fin_de_semana = inicio_de_semana + timedelta(days=6)
            blocks = Block_de_espuma.objects.filter(creado__range =[inicio_de_semana, fin_de_semana])
        else:
            blocks= Block_de_espuma.objects.all()
    context= {'blocks':blocks}
    return render(request, "inventario/index.html",context)

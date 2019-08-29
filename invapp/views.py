from django.shortcuts import render
from .models import Block_de_espuma
from django.http import HttpResponse

# Create your views here.

def index(request):
    blocks= Block_de_espuma.objects.all()
    context= {'blocks':blocks}
    return render(request, "inventario/index.html",context)

from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    topicos = Topico.objects.all()
    return render(request, 'home.html', {'topicos': topicos})

def exibir_topico(request, topico_id):
    topico = get_object_or_404(Topico, id=topico_id)
    return render(request, 'topico.html', {'topico': topico})
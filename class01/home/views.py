from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    topicos = Topico.objects.all()
    new_suport_form = []
    search = request.GET.get('search')
    if search:
        topicos = Topico.objects.filter(nome_topico__icontains=search)

    if request.method == 'POST':
        new_suport_form = SuporteModelForm(request.POST)
        if new_suport_form.is_valid():
            new_suport_form.save()
            return redirect('home')
        
        else:
            new_suport_form = SuporteModelForm()

    context = {'topicos': topicos, 'form': new_suport_form}

    return render(request, 'home.html', context)

def exibir_topico(request, topico_id):
    topico = get_object_or_404(Topico, id=topico_id)
    return render(request, 'topico.html', {'topico': topico})
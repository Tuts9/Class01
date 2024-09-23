from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def home(request):
    topicos = Topico.objects.order_by('?')[:6]
    new_suport_form = []
    
    if request.method == 'POST':
        new_suport_form = SuporteModelForm(request.POST)
        if new_suport_form.is_valid():
            new_suport_form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('home')
        
    else:
        new_suport_form = SuporteModelForm()

    context = {'topicos': topicos, 'form': new_suport_form}

    return render(request, 'home.html', context)

def all_topics(request):
    topicos = Topico.objects.all()
    form_topic = FiltroTopico(request.GET)

    if form_topic.is_valid():
        categoria = form_topic.cleaned_data['categoria']
        nivel_experiencia = form_topic.cleaned_data['nivel_experiencia']
        funcao = form_topic.cleaned_data['funcao']
        ordernar_por = form_topic.cleaned_data['ordenar_por']
        search = request.GET.get('search')
    
        if search:
            topicos = Topico.objects.filter(nome_topico__icontains=search)

        if categoria:
            topicos = Topico.objects.filter(categorias=categoria)
        
        if nivel_experiencia:
            topicos = Topico.objects.filter(nivel_experiencia=nivel_experiencia)

        if funcao:
            topicos = Topico.objects.filter(funcao=funcao)

        if ordernar_por:
            topicos = Topico.objects.order_by(ordernar_por)

        redirect('all_topics')

    context = {'topicos': topicos, 'form_topic': form_topic}

    return render(request, 'all_topics.html', context)

def topic_list(request, topico_id):
    current_topic = get_object_or_404(Topico, id=topico_id)
    ferramentas = Ferramenta.objects.filter(topico=current_topic)

    try:
        next_topic = Topico.objects.filter(id__gt=current_topic.id).order_by('id').first()
    except Topico.DoesNotExist:
        next_topic = None

    try:
        previous_topic = Topico.objects.filter(id__lt=current_topic.id).order_by('-id').first()
    except Topico.DoesNotExist:
        previous_topic = None

    context = {'current_topic': current_topic,
               'ferramentas': ferramentas,
               'next_topic': next_topic,
               'previous_topic': previous_topic}

    return render(request, 'topico.html', context)


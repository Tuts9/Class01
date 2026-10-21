from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST

from .forms import *
from .models import *


def home(request):
    topicos = Topico.objects.order_by('?')[:4]
    form_topic = FiltroTopico(request.GET)
    search = request.GET.get('search')
    first_topic = Topico.objects.order_by('id').first()
    first_item = first_topic.id if first_topic else None

    if search:
        topicos = Topico.objects.filter(nome_topico__icontains=search)
        context = {'topicos': topicos, 'form_topic': form_topic}
        return render(request, 'all_topics.html', context)

    if request.method == 'POST':
        new_suport_form = SuporteModelForm(request.POST)
        if new_suport_form.is_valid():
            new_suport_form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('home')
    else:
        new_suport_form = SuporteModelForm()

    trilhas = Trilha.objects.filter(ativa=True)[:3]

    context = {
        'topicos': topicos,
        'form': new_suport_form,
        'first_item': first_item,
        'trilhas': trilhas,
    }
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
            topicos = topicos.filter(nome_topico__icontains=search)
        if categoria:
            topicos = topicos.filter(categorias=categoria)
        if nivel_experiencia:
            topicos = topicos.filter(nivel_experiencia=nivel_experiencia)
        if funcao:
            topicos = topicos.filter(funcao=funcao)
        if ordernar_por:
            topicos = topicos.order_by(ordernar_por)

    context = {'topicos': topicos, 'form_topic': form_topic}
    return render(request, 'all_topics.html', context)


def topic_list(request, topico_id):
    current_topic = get_object_or_404(Topico, id=topico_id)
    ferramentas = Ferramenta.objects.filter(topico=current_topic)
    form_topic = FiltroTopico(request.GET)
    search = request.GET.get('search')
    topicos = Topico.objects.all()

    if search:
        topicos = Topico.objects.filter(nome_topico__icontains=search)
        context = {'topicos': topicos, 'form_topic': form_topic}
        return render(request, 'all_topics.html', context)

    next_topic = Topico.objects.filter(id__gt=current_topic.id).order_by('id').first()
    previous_topic = Topico.objects.filter(id__lt=current_topic.id).order_by('-id').first()

    context = {
        'current_topic': current_topic,
        'ferramentas': ferramentas,
        'next_topic': next_topic,
        'previous_topic': previous_topic,
        'topicos': topicos,
    }
    return render(request, 'topico.html', context)


def trilhas_list(request):
    trilhas = Trilha.objects.filter(ativa=True)
    trilhas_data = []
    for trilha in trilhas:
        trilhas_data.append({
            'trilha': trilha,
            'progresso': trilha.progresso_percentual(request.user) if request.user.is_authenticated else None,
        })

    context = {'trilhas_data': trilhas_data}
    return render(request, 'trilhas.html', context)


def trilha_detail(request, slug):
    trilha = get_object_or_404(Trilha, slug=slug, ativa=True)
    etapas = trilha.etapas.select_related('topico').all()
    concluidas_ids = set()
    if request.user.is_authenticated:
        concluidas_ids = set(
            ProgressoUsuario.objects.filter(
                usuario=request.user,
                etapa__trilha=trilha,
                concluida=True,
            ).values_list('etapa_id', flat=True)
        )

    etapas_com_status = [
        {'etapa': etapa, 'concluida': etapa.id in concluidas_ids}
        for etapa in etapas
    ]

    context = {
        'trilha': trilha,
        'etapas_com_status': etapas_com_status,
        'progresso': trilha.progresso_percentual(request.user) if request.user.is_authenticated else 0,
        'total': etapas.count(),
        'concluidas': len(concluidas_ids),
    }
    return render(request, 'trilha_detail.html', context)


@login_required
@require_POST
def toggle_etapa(request, etapa_id):
    etapa = get_object_or_404(EtapaTrilha, id=etapa_id)
    progresso, _ = ProgressoUsuario.objects.get_or_create(
        usuario=request.user,
        etapa=etapa,
    )
    progresso.concluida = not progresso.concluida
    progresso.save()
    return redirect('trilha_detail', slug=etapa.trilha.slug)


def registro(request):
    if request.user.is_authenticated:
        return redirect('conta')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada! Acompanhe seu progresso nas trilhas.')
            return redirect('trilhas_list')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


class Class01LoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True


@require_http_methods(['GET', 'POST'])
def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da conta.')
    return redirect('home')


@login_required
def conta(request):
    trilhas = Trilha.objects.filter(ativa=True)
    resumo = []
    continuar = None
    for trilha in trilhas:
        pct = trilha.progresso_percentual(request.user)
        concluidas = ProgressoUsuario.objects.filter(
            usuario=request.user,
            etapa__trilha=trilha,
            concluida=True,
        ).count()
        total = trilha.total_etapas()
        item = {
            'trilha': trilha,
            'percentual': pct,
            'concluidas': concluidas,
            'total': total,
        }
        resumo.append(item)
        if continuar is None and pct < 100 and total > 0:
            proxima = (
                trilha.etapas.exclude(
                    progressos__usuario=request.user,
                    progressos__concluida=True,
                )
                .order_by('ordem')
                .first()
            )
            if proxima:
                continuar = {'trilha': trilha, 'etapa': proxima}

    context = {
        'resumo': resumo,
        'continuar': continuar,
    }
    return render(request, 'conta.html', context)

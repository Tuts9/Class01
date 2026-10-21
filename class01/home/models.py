from django.conf import settings
from django.db import models


NIVEL_CHOICES = [
    ('Iniciante', 'Iniciante'),
    ('Intermediário', 'Intermediário'),
    ('Avançado', 'Avançado'),
]


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class AreaAtuacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Topico(models.Model):
    icon_topico = models.ImageField(upload_to='img/icon_topic/')
    nome_topico = models.CharField(max_length=50)
    categorias = models.ManyToManyField(Categoria, related_name='topicos')
    introducao = models.TextField()
    imagem = models.ImageField(upload_to='img/image_topic/')
    fonte_topic = models.URLField()
    nivel_experiencia = models.CharField(max_length=100, choices=NIVEL_CHOICES)
    funcao = models.ManyToManyField(AreaAtuacao, related_name='topicos')
    ferramentas = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_topico


class Ferramenta(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.PROTECT, related_name='ferramentas_relacionadas')
    nome_ferramenta = models.CharField(max_length=50)
    imagem_ferramenta = models.ImageField(upload_to='img/image_ferramenta/')
    informacao_ferramenta = models.TextField()
    link_ferramenta = models.URLField()

    def __str__(self) -> str:
        return f'{self.topico} / {self.nome_ferramenta}'


class Erro(models.Model):
    id = models.AutoField(primary_key=True)
    nome_erro = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome_erro


class Suporte(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('email', max_length=100)
    assunto = models.ForeignKey(Erro, on_delete=models.PROTECT, related_name='tipo_erro')
    mensagem = models.TextField()

    def __str__(self) -> str:
        return f'{self.assunto} / {self.mensagem}'


class Trilha(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descricao = models.TextField()
    icone = models.ImageField(upload_to='img/trilha/', blank=True, null=True)
    nivel_alvo = models.CharField(max_length=100, choices=NIVEL_CHOICES, default='Iniciante')
    ordem = models.PositiveIntegerField(default=0)
    ativa = models.BooleanField(default=True)

    class Meta:
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome

    def total_etapas(self):
        return self.etapas.count()

    def progresso_percentual(self, user):
        total = self.total_etapas()
        if not total or not user.is_authenticated:
            return 0
        concluidas = ProgressoUsuario.objects.filter(
            usuario=user,
            etapa__trilha=self,
            concluida=True,
        ).count()
        return int((concluidas / total) * 100)


class EtapaTrilha(models.Model):
    trilha = models.ForeignKey(Trilha, on_delete=models.CASCADE, related_name='etapas')
    ordem = models.PositiveIntegerField(default=0)
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    topico = models.ForeignKey(
        Topico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='etapas_trilha',
    )
    link_externo = models.URLField(blank=True)

    class Meta:
        ordering = ['ordem', 'id']
        unique_together = [('trilha', 'ordem')]

    def __str__(self):
        return f'{self.trilha.nome} — {self.ordem}. {self.titulo}'


class ProgressoUsuario(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='progressos',
    )
    etapa = models.ForeignKey(EtapaTrilha, on_delete=models.CASCADE, related_name='progressos')
    concluida = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('usuario', 'etapa')]
        verbose_name_plural = 'Progressos dos usuários'

    def __str__(self):
        status = 'concluída' if self.concluida else 'pendente'
        return f'{self.usuario} — {self.etapa} ({status})'

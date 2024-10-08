from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

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
    introducao = tinymce_models.HTMLField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    imagem = models.ImageField(upload_to='img/image_topic/')
    fonte_topic = models.URLField()
    nivel_experiencia = models.CharField(max_length=100, choices=[
        ('Iniciante', 'Iniciante'),
        ('Intermediário', 'Intermediário'),
        ('Avançado', 'Avançado')
    ])
    funcao = models.ManyToManyField(AreaAtuacao, related_name='topicos')
    ferramentas = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nome_topico} / {self.autor}'
    
    def get_absolute_url(self):
        return reverse('home')

class Ferramenta(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.PROTECT)
    nome_ferramenta = models.CharField(max_length=50)
    imagem_ferramenta = models.ImageField(upload_to='img/image_ferramenta/')
    informacao_ferramenta = tinymce_models.HTMLField()
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
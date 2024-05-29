from django.db import models

# Create your models here.
class Topico(models.Model):
    icon_topico = models.ImageField(upload_to='img/icons/', null=True, blank=True)
    nome_topico = models.CharField(max_length=50)
    introducao = models.TextField()
    imagem = models.ImageField(upload_to='img/')
    fonte = models.URLField()
    texto_ferramenta = models.TextField()
    fonte_ferramenta = models.URLField()

    def __str__(self) -> str:
        return self.nome_topico
    
class Ferramenta(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.PROTECT)
    nome_ferramenta = models.CharField(max_length=50)
    imagem_ferramenta = models.ImageField(upload_to='img/ferramenta/')
    informacao_ferramenta = models.TextField()
    link_ferramenta = models.URLField()

    def __str__(self) -> str:
        return self.nome_ferramenta

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
        return f'{self.assunto}'
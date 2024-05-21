from django.db import models

# Create your models here.
class Topico(models.Model):
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
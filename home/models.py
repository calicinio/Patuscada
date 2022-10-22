from django.db import models

# Create your models here.

class onde_ficar(models.Model):
    descricao = models.CharField(max_length = 50)
    contato = models.CharField(max_length = 50)
    falarCom = models.CharField(max_length = 50)
from django.db import models

class Book(models.Model):
    nome = models.CharField(max_length= 50)
    imagem = models.ImageField()
    autor = models.CharField(max_length= 30, default='desconhecido')
    email = models.EmailField(blank= True)
    descricao = models.TextField(default='Sem descrição')

    def __str__(self):
        return self.name
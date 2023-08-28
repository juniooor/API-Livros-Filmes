from django.db import models

# Create your models here.

class Book(models.Model):
    autor = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    lancamento = models.IntegerField(max_length=4)

    def __str__(self):
        return self.nome
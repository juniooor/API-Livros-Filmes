from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=40)
    autor = models.CharField(max_length=70)
    lancamento = models.IntegerField()
    
    def __str__(self):
        return self.title
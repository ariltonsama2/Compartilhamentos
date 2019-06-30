from django.db import models
from django.urls import reverse

#Model para o Form Game
class Game(models.Model):
    name = models.CharField(max_length=200)
    contato = models.CharField(max_length=50)
    originalum = models.FloatField(default=0)
    originaldois = models.FloatField(default=0)
    fantasma = models.FloatField(default=0)
    senha = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Games_fbv:Game_edit', kwargs={'pk': self.pk})
    
    
    
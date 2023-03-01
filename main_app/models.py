from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    weakness = models.CharField(max_length=100)

    def __str__(self): 
        return f'{self.name} ({self.id})'
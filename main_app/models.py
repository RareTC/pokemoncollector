from django.db import models
from django.urls import reverse
from datetime import date
from datetime import timedelta

POKEBALLS = (
    ('P', 'Pokeball'),
    ('G', 'Great ball'),
    ('M', 'Master ball'),
    ('N', 'Net ball'),
)

class Move(models.Model):
  name = models.CharField(max_length=50)
  level = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('moves_detail', kwargs={'pk': self.id})

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    weakness = models.CharField(max_length=100)
    moves = models.ManyToManyField(Move)

    def __str__(self): 
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})
    
    def caught(self):
        return self.captured_set.filter(date__lte=(date.today() - timedelta(days=1)))
    
class Captured(models.Model):
    date = models.DateField('Captured Date')
    pokeball = models.CharField(
        max_length=1,
        choices=POKEBALLS,
        default=POKEBALLS[0][0]
        )
    
    # Create a FK 
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Caught with {self.get_pokeball_display()} on {self.date}"

    class Meta:
        # descending order for date
        ordering = ['-date']
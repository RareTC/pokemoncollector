from django.shortcuts import render

# a baby step to make a local model for learning purposes. 
pokemons = [
  {'name': 'Eevee', 'type': 'normal', 'description': 'furry and little', 'weaknesses': 'Fighting'},
  {'name': 'Squirtle', 'type': 'water', 'description': 'turtle-like with a round tail', 'weaknesses': 'Grass and Electric'},
]

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
    return render(request, 'pokemons/index.html', {
        'pokemons' : pokemons
    })
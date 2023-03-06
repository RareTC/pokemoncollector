from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Move
from .forms import CapturedForm

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemons/index.html', {  'pokemons' : pokemons  })

def pokemons_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    id_list = pokemon.moves.all().values_list('id')
    moves_pokemon_doesnt_have = Move.objects.exclude(id__in=id_list)
    # render CapturedForm in HTML
    captured_form = CapturedForm()
    return render(request, 'pokemons/detail.html', { 
        'pokemon' : pokemon, 'captured_form' : captured_form,
        'moves' : moves_pokemon_doesnt_have
    })

class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'kind', 'description', 'weakness' ]

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = '__all__'
    
class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon'

def add_capture(request, pokemon_id):
    form = CapturedForm(request.POST)
    if form.is_valid():
        new_capture = form.save(commit=False)
        new_capture.pokemon_id = pokemon_id
        new_capture.save()
    return redirect('detail', pokemon_id=pokemon_id)

class MoveList(ListView):
  model = Move

class MoveDetail(DetailView):
  model = Move

class MoveCreate(CreateView):
  model = Move
  fields = '__all__'

class MoveUpdate(UpdateView):
  model = Move
  fields = ['name', 'level']

class MoveDelete(DeleteView):
  model = Move
  success_url = '/moves'

def assoc_move(request, pokemon_id, move_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Pokemon.objects.get(id=pokemon_id).moves.add(move_id)
  return redirect('detail', pokemon_id=pokemon_id)


def unassoc_move(request, pokemon_id, move_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Pokemon.objects.get(id=pokemon_id).moves.remove(move_id)
  return redirect('detail', pokemon_id=pokemon_id)
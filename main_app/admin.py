from django.contrib import admin
from .models import Pokemon, Captured, Move

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Captured)
admin.site.register(Move)
from django.forms import ModelForm
from .models import Captured

class CapturedForm(ModelForm):
    class Meta:
        model = Captured
        fields = ['date', 'pokeball']
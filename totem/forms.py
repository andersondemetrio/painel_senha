from django import forms
from totem.models import Totem

class TotemForm(forms.ModelForm):
    class Meta:
        model = Totem
        files =("__all__")
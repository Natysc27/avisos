from django import from .forms import
from .models import Aviso

class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ['titulo', 'conteudo', 'categoria']
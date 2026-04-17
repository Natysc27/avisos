from django.shortcuts import render
from .models import Aviso

# Create your views here.
def lista_avisos(request):
    """Exibe todos os avisos, agora usando o filtro por ForeingnKey."""
    avisos = Aviso.objects.all().order_by('-data_criacao')

    # O filtro agora busca pelo ID ouSlug da categoria
    # Exemplo: ?categoria=1 (filtra pelo ID da categoria)
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        avisos = avisos.filter(categoria_id=categoria_id)

    return render(request, 'mural/lista_avisos.html', {'avisos': avisos})

def detalhe_aviso(request, id):
    """Busca o aviso e o Django automaticamente traz  a categoria relacionada."""
    aviso = get_object_or_404(Aviso, id=id)
    return render(request, 'mural/detalhe_aviso.html', {'aviso': aviso})


def criar_aviso(request):
    """O ModelForm irá gerar automaticamente um <select> com as Categorias."""
    if request. == "POST":
        form = AvisoForm(request.POST)
        if form.is_valid()
        return redirect('home')
    else:
           form = AvisoForm()
    return render(request, 'mural/form_aviso.html', {'form': form})

           pass
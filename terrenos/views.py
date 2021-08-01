from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

class formulario_fiscal(ModelForm):
    class Meta:
        model = Fiscal
        fields = ['nome_fiscal', 'matricula_fiscal', 'nivel', 'primeiro_nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matricula_fiscal'].widget.attrs.update({'class':'mask-matricula'})

# Cria a função de cadastrar um estado
def cadastrar_fiscal(request, template_name='fiscal/formulario_fiscal.html'):
    form = formulario_fiscal(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_fiscal')
    return render(request, template_name, {'form': form})

def listar_fiscal(request, template_name="fiscal/listar_fiscal.html"):
    query = request.GET.get("busca")
    if query:
        fiscal = Fiscal.objects.filter(nome_fiscal__icontains=query)
    else:
        fiscal = Fiscal.objects.all()
    fiscais = {'lista': fiscal}
    return render(request, template_name, fiscais)


# Cria a função de editar um estado
def editar_fiscal(request, pk, template_name='fiscal/formulario_fiscal.html'):
    fiscal = get_object_or_404(Fiscal, pk=pk)
    if request.method == "POST":
        form = formulario_fiscal(request.POST, instance=fiscal)
        if form.is_valid():
            fiscal = form.save()
            return redirect('listar_fiscal')
    else:
        form = formulario_fiscal(instance=fiscal)
    return render(request, template_name, {'form': form})



# Cria a função de deletar um estado
def excluir_fiscal(request, pk):
    fiscal = Fiscal.objects.get(pk=pk)
    if request.method == "POST":
        fiscal.delete()
        return redirect('listar_fiscal')
    return render(request, 'fiscal/excluir_fiscal.html', {'fiscal': fiscal})


def homepage(request, template_name="base.html"):
    return render(request, template_name)

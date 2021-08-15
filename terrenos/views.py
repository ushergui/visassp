from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from datetime import date, timedelta


class formulario_proprietario(ModelForm):
    class Meta:
        model = Proprietario
        fields = ['nome_proprietario', 'logradouro_proprietario', 'numero_proprietario','complemento_proprietario',
                  'bairro_proprietario','cep_proprietario','municipio_proprietario','estado_proprietario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cep_proprietario'].widget.attrs.update({'class': 'mask-cep'})

# Cria a função de cadastrar um estado
def cadastrar_proprietario(request, template_name='proprietario/formulario_proprietario.html'):
    form = formulario_proprietario(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_proprietario')
    return render(request, template_name, {'form': form})


# Cria a função de listar os estados
#def listar_proprietario(request, template_name='proprietario/listar_proprietario.html'):
    #   proprietario = Proprietario.objects.all()
    #proprietarios = {'lista': proprietario}
    #return render(request, template_name, proprietarios)

def listar_proprietario(request, template_name="proprietario/listar_proprietario.html"):
    query = request.GET.get("busca")
    if query:
        proprietario = Proprietario.objects.filter(nome_proprietario__icontains=query)
    else:
        proprietario = Proprietario.objects.all()
    proprietarios = {'lista': proprietario}
    return render(request, template_name, proprietarios)



# Cria a função de deletar um estado
def excluir_proprietario(request, pk):
    proprietario = Proprietario.objects.get(pk=pk)
    if request.method == "POST":
        proprietario.delete()
        return redirect('listar_proprietario')
    return render(request, 'proprietario/excluir_proprietario.html', {'proprietario': proprietario})



# Cria a função de editar um estado
def editar_proprietario(request, pk, template_name='proprietario/formulario_proprietario.html'):
    proprietario = get_object_or_404(Proprietario, pk=pk)
    if request.method == "POST":
        form = formulario_proprietario(request.POST, instance=proprietario)
        if form.is_valid():
            proprietario = form.save()
            return redirect('listar_proprietario')
    else:
        form = formulario_proprietario(instance=proprietario)
    return render(request, template_name, {'form': form})


#terrenoS:

class formulario_terreno(ModelForm):
    class Meta:
        model = Terreno
        fields = ['inscricao_terreno', 'logradouro_terreno', 'numero_terreno',
                  'bairro_terreno','cep_terreno','municipio_terreno','estado_terreno','proprietario', 'lote_terreno',
                  'quadra_terreno', 'area_terreno','logradouro_correspondencia','numero_correspondencia',
                  'complemento_correspondencia', 'bairro_correspondencia','cep_correspondencia',
                  'municipio_correspondencia','estado_correspondencia']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cep_correspondencia'].widget.attrs.update({'class': 'mask-cep'})

# Cria a função de cadastrar um estado
def cadastrar_terreno(request, template_name='terreno/formulario_terreno.html'):
    form = formulario_terreno(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_terreno')
    return render(request, template_name, {'form': form})


# Cria a função de listar os estados
#def listar_terreno(request, template_name='terreno/listar_terreno.html'):
    #terreno = Terreno.objects.all()
    #terrenos = {'lista': terreno}
   # return render(request, template_name, terrenos)


def listar_terreno(request, template_name="terreno/listar_terreno.html"):
    query = request.GET.get("busca")

    if query:
        terreno = Terreno.objects.filter(inscricao_terreno__icontains=query)
    else:
        terreno = Terreno.objects.all()
    terrenos = {'lista': terreno}
    return render(request, template_name, terrenos)





# Cria a função de deletar um estado
def excluir_terreno(request, pk):
    terreno = Terreno.objects.get(pk=pk)
    if request.method == "POST":
        terreno.delete()
        return redirect('listar_terreno')
    return render(request, 'terreno/excluir_terreno.html', {'terreno': terreno})



# Cria a função de editar um estado
def editar_terreno(request, pk, template_name='terreno/formulario_terreno.html'):
    terreno = get_object_or_404(Terreno, pk=pk)
    if request.method == "POST":
        form = formulario_terreno(request.POST, instance=terreno)
        if form.is_valid():
            terreno = form.save()
            return redirect('listar_terreno')
    else:
        form = formulario_terreno(instance=terreno)
    return render(request, template_name, {'form': form})


class formulario_protocolo(ModelForm):
    class Meta:
        model = Protocolo
        fields = ['protocolo', 'solicitante_protocolo', 'logradouro_protocolo','bairro_protocolo',
                  'descricao_protocolo','status_protocolo','entrada_protocolo','encerramento_protocolo','fiscal']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['protocolo'].widget.attrs.update({'class': 'mask-protocolo'})

# Cria a função de cadastrar um estado
def cadastrar_protocolo(request, template_name='protocolo/formulario_protocolo.html'):
    form = formulario_protocolo(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_protocolo')
    return render(request, template_name, {'form': form})


# Cria a função de listar os estados
# def listar_protocolo(request, template_name='protocolo/listar_protocolo.html'):
    #  protocolo = Protocolo.objects.all()
    # protocolos = {'lista': protocolo}
    # return render(request, template_name, protocolos)

def listar_protocolo(request, template_name="protocolo/listar_protocolo.html"):
    query = request.GET.get("busca")
    if query:
        protocolo = Protocolo.objects.filter(protocolo__icontains=query)
    else:
        protocolo = Protocolo.objects.all()
    protocolos = {'lista': protocolo}
    return render(request, template_name, protocolos)



# Cria a função de deletar um estado
def excluir_protocolo(request, pk):
    protocolo = Protocolo.objects.get(pk=pk)
    if request.method == "POST":
        protocolo.delete()
        return redirect('listar_protocolo')
    return render(request, 'protocolo/excluir_protocolo.html', {'protocolo': protocolo})



# Cria a função de editar um estado
def editar_protocolo(request, pk, template_name='protocolo/formulario_protocolo.html'):
    protocolo = get_object_or_404(Protocolo, pk=pk)
    if request.method == "POST":
        form = formulario_protocolo(request.POST, instance=protocolo)
        if form.is_valid():
            protocolo = form.save()
            return redirect('listar_protocolo')
    else:
        form = formulario_protocolo(instance=protocolo)
    return render(request, template_name, {'form': form})



class formulario_notificacao(ModelForm):
    class Meta:
        model = Notificacao
        fields = ['protocolo', 'terreno','data_notificacao',
                  'data_inspecao','horario_inspecao','fiscal', 'rastreio_notificacao','data_entrega_notificacao','data_retorno','horario_retorno','observacoes','cumpriu_notificacao']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rastreio_notificacao'].widget.attrs.update({'class': 'mask-rastreio'})
        self.fields['data_entrega_notificacao'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_retorno'].widget.attrs.update({'class': 'mask-date'})
        self.fields['horario_retorno'].widget.attrs.update({'class': 'mask-time'})
        self.fields['data_inspecao'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_notificacao'].widget.attrs.update({'class': 'mask-date'})
        self.fields['horario_inspecao'].widget.attrs.update({'class': 'mask-time'})

# Cria a função de cadastrar um estado
def cadastrar_notificacao(request, template_name='notificacao/formulario_notificacao.html'):
    form = formulario_notificacao(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_notificacao')
    return render(request, template_name, {'form': form})


# Cria a função de listar os estados
#def listar_notificacao(request, template_name='notificacao/listar_notificacao.html'):
 #   notificacao = Notificacao.objects.all()
  #  notificacoes = {'lista': notificacao}
   # return render(request, template_name, notificacoes)

def listar_notificacao(request, template_name="notificacao/listar_notificacao.html"):
    query = request.GET.get("busca")
    if query:
        notificacao = Notificacao.objects.filter(id__icontains=query)
    else:
        notificacao = Notificacao.objects.all()

    notificacoes = {'lista': notificacao}
    return render(request, template_name, notificacoes)



def gerar_notificacao(request,pk,template_name="notificacao/gerar_notificacao.html"):
    notificacao = get_object_or_404(Notificacao, pk=pk)
    return render(request, template_name, {'notificacao':notificacao})

def gerar_ar(request,pk,template_name="notificacao/gerar_ar.html"):
    notificacao = get_object_or_404(Notificacao, pk=pk)
    return render(request, template_name, {'notificacao':notificacao})

def gerar_ar2(request,pk,template_name="notificacao/gerar_ar2.html"):
    notificacao = get_object_or_404(Notificacao, pk=pk)
    return render(request, template_name, {'notificacao':notificacao})



# Cria a função de deletar um estado
def excluir_notificacao(request, pk):
    notificacao = Notificacao.objects.get(pk=pk)
    if request.method == "POST":
        notificacao.delete()
        return redirect('listar_notificacao')
    return render(request, 'notificacao/excluir_notificacao.html', {'notificacao': notificacao})



# Cria a função de editar um estado
def editar_notificacao(request, pk, template_name='notificacao/formulario_notificacao.html'):
    notificacao = get_object_or_404(Notificacao, pk=pk)
    if request.method == "POST":
        form = formulario_notificacao(request.POST, instance=notificacao)
        if form.is_valid():
            notificacao = form.save()
            return redirect('listar_notificacao')
    else:
        form = formulario_notificacao(instance=notificacao)
    return render(request, template_name, {'form': form})


class formulario_infracao(ModelForm):
    class Meta:
        model = Infracao
        fields = ['notificacao', 'data_auto','data_inspecao_2',
                  'horario_inspecao_2','rastreio_infracao','data_entrega_autuacao', 'defendeu']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rastreio_infracao'].widget.attrs.update({'class': 'mask-rastreio'})
        self.fields['data_auto'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_inspecao_2'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_entrega_autuacao'].widget.attrs.update({'class': 'mask-date'})
        self.fields['horario_inspecao_2'].widget.attrs.update({'class': 'mask-time'})


# Cria a função de cadastrar um estado
def cadastrar_infracao(request, template_name='infracao/formulario_infracao.html'):
    form = formulario_infracao(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_infracao')
    return render(request, template_name, {'form': form})


# Cria a função de listar os estados
#def listar_notificacao(request, template_name='notificacao/listar_notificacao.html'):
 #   notificacao = Notificacao.objects.all()
  #  notificacoes = {'lista': notificacao}
   # return render(request, template_name, notificacoes)

def listar_infracao(request, template_name="infracao/listar_infracao.html"):
    query = request.GET.get("busca")
    if query:
        infracao = Infracao.objects.filter(id__icontains=query)
    else:
        infracao = Infracao.objects.all()

    infracoes = {'lista': infracao}
    return render(request, template_name, infracoes)



def gerar_infracao(request,pk,template_name="infracao/gerar_infracao.html"):
    infracao = get_object_or_404(Infracao, pk=pk)
    return render(request, template_name, {'infracao':infracao})

def gerar_ar_inf(request,pk,template_name="infracao/gerar_ar_inf.html"):
    infracao = get_object_or_404(Infracao, pk=pk)
    return render(request, template_name, {'infracao':infracao})

def gerar_ar2_inf(request,pk,template_name="infracao/gerar_ar2_inf.html"):
    infracao = get_object_or_404(Infracao, pk=pk)
    return render(request, template_name, {'infracao':infracao})



# Cria a função de deletar um estado
def excluir_infracao(request, pk):
    infracao = Infracao.objects.get(pk=pk)
    if request.method == "POST":
        infracao.delete()
        return redirect('listar_infracao')
    return render(request, 'infracao/excluir_infracao.html', {'infracao': infracao})



# Cria a função de editar um estado
def editar_infracao(request, pk, template_name='infracao/formulario_infracao.html'):
    infracao = get_object_or_404(Infracao, pk=pk)
    if request.method == "POST":
        form = formulario_infracao(request.POST, instance=infracao)
        if form.is_valid():
            infracao = form.save()
            return redirect('listar_infracao')
    else:
        form = formulario_infracao(instance=infracao)
    return render(request, template_name, {'form': form})

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


# Cria a função de listar os estados
#def listar_fiscal(request, template_name='fiscal/listar_fiscal.html'):
    #fiscal = Fiscal.objects.all()
   # fiscais = {'lista': fiscal}
   # return render(request, template_name, fiscais)

def listar_fiscal(request, template_name="fiscal/listar_fiscal.html"):
    query = request.GET.get("busca")
    if query:
        fiscal = Fiscal.objects.filter(nome_fiscal__icontains=query)
    else:
        fiscal = Fiscal.objects.all()
    fiscais = {'lista': fiscal}
    return render(request, template_name, fiscais)



# Cria a função de deletar um estado
def excluir_fiscal(request, pk):
    fiscal = Fiscal.objects.get(pk=pk)
    if request.method == "POST":
        fiscal.delete()
        return redirect('listar_fiscal')
    return render(request, 'fiscal/excluir_fiscal.html', {'fiscal': fiscal})



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


def homepage(request, template_name="base.html"):
    return render(request, template_name)

def test(request, template_name="test.html"):
    return render(request, template_name)






from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    url(r'^cadastrar_fiscal', cadastrar_fiscal, name='cadastrar_fiscal'),
    url(r'^listar_fiscal', listar_fiscal, name='listar_fiscal'),
    url(r'^excluir_fiscal/(?P<pk>[0-9]+)', excluir_fiscal, name='excluir_fiscal'),
    url(r'^editar_fiscal/(?P<pk>[0-9]+)', editar_fiscal, name='editar_fiscal'),
    url(r"^$", homepage, name='homepage'),

]
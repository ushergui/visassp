from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [

    url(r"^$", homepage, name='homepage'),
    url(r'^cadastrar_fiscal', cadastrar_fiscal, name='cadastrar_fiscal'),
    url(r'^listar_fiscal', listar_fiscal, name='listar_fiscal'),
    url(r'^excluir_fiscal/(?P<pk>[0-9]+)', excluir_fiscal, name='excluir_fiscal'),
    url(r'^editar_fiscal/(?P<pk>[0-9]+)', editar_fiscal, name='editar_fiscal'),
    url(r'^cadastrar_notificacao', cadastrar_notificacao, name='cadastrar_notificacao'),
    url(r'^listar_notificacao', listar_notificacao, name='listar_notificacao'),
    url(r'^excluir_notificacao/(?P<pk>[0-9]+)', excluir_notificacao, name='excluir_notificacao'),
    url(r'^gerar_notificacao/(?P<pk>[0-9]+)', gerar_notificacao, name='gerar_notificacao'),
    url(r'^editar_notificacao/(?P<pk>[0-9]+)', editar_notificacao, name='editar_notificacao'),
    url(r'^cadastrar_proprietario', cadastrar_proprietario, name='cadastrar_proprietario'),
    url(r'^listar_proprietario', listar_proprietario, name='listar_proprietario'),
    url(r'^excluir_proprietario/(?P<pk>[0-9]+)', excluir_proprietario, name='excluir_proprietario'),
    url(r'^editar_proprietario/(?P<pk>[0-9]+)', editar_proprietario, name='editar_proprietario'),
    url(r'^cadastrar_protocolo', cadastrar_protocolo, name='cadastrar_protocolo'),
    url(r'^listar_protocolo', listar_protocolo, name='listar_protocolo'),
    url(r'^excluir_protocolo/(?P<pk>[0-9]+)', excluir_protocolo, name='excluir_protocolo'),
    url(r'^editar_protocolo/(?P<pk>[0-9]+)', editar_protocolo, name='editar_protocolo'),
    url(r'^cadastrar_terreno', cadastrar_terreno, name='cadastrar_terreno'),
    url(r'^listar_terreno', listar_terreno, name='listar_terreno'),
    url(r'^excluir_terreno/(?P<pk>[0-9]+)', excluir_terreno, name='excluir_terreno'),
    url(r'^editar_terreno/(?P<pk>[0-9]+)', editar_terreno, name='editar_terreno'),

]
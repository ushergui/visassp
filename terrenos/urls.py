from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    #endereço, a View, nome da url
    url(r"^$", homepage, name='homepage'),
    url(r"^test", test, name='test'),
    url(r'^cadastrar_fiscal', cadastrar_fiscal, name='cadastrar_fiscal'),
    url(r'^listar_fiscal', listar_fiscal, name='listar_fiscal'),
    url(r'^excluir_fiscal/(?P<pk>[0-9]+)', excluir_fiscal, name='excluir_fiscal'),
    url(r'^editar_fiscal/(?P<pk>[0-9]+)', editar_fiscal, name='editar_fiscal'),
    url(r'^cadastrar_notificacao', cadastrar_notificacao, name='cadastrar_notificacao'),
    url(r'^listar_notificacao', listar_notificacao, name='listar_notificacao'),
    url(r'^excluir_notificacao/(?P<pk>[0-9]+)', excluir_notificacao, name='excluir_notificacao'),
    url(r'^gerar_notificacao/(?P<pk>[0-9]+)', gerar_notificacao, name='gerar_notificacao'),
    url(r'^editar_notificacao/(?P<pk>[0-9]+)', editar_notificacao, name='editar_notificacao'),
    url(r'^cadastrar_inspecao', cadastrar_inspecao, name='cadastrar_inspecao'),
    url(r'^listar_inspecao', listar_inspecao, name='listar_inspecao'),
    url(r'^excluir_inspecao/(?P<pk>[0-9]+)', excluir_inspecao, name='excluir_inspecao'),
    url(r'^editar_inspecao/(?P<pk>[0-9]+)', editar_inspecao, name='editar_inspecao'),
    url(r'^gerar_inspecao/(?P<pk>[0-9]+)', gerar_inspecao, name='gerar_inspecao'),
    url(r'^gerar_ar/(?P<pk>[0-9]+)', gerar_ar, name='gerar_ar'),
    url(r'^gerar_ar2/(?P<pk>[0-9]+)', gerar_ar2, name='gerar_ar2'),
    url(r'^gerar_ar3/(?P<pk>[0-9]+)', gerar_ar3, name='gerar_ar3'),
    url(r'^cadastrar_infracao', cadastrar_infracao, name='cadastrar_infracao'),
    url(r'^listar_infracao', listar_infracao, name='listar_infracao'),
    url(r'^excluir_infracao/(?P<pk>[0-9]+)', excluir_infracao, name='excluir_infracao'),
    url(r'^gerar_infracao/(?P<pk>[0-9]+)', gerar_infracao, name='gerar_infracao'),
    url(r'^ver_protocolo/(?P<pk>[0-9]+)', ver_protocolo, name='ver_protocolo'),
    url(r'^gerar_ar_inf/(?P<pk>[0-9]+)', gerar_ar_inf, name='gerar_ar_inf'),
    url(r'^gerar_ar_inf2/(?P<pk>[0-9]+)', gerar_ar_inf2, name='gerar_ar_inf2'),
    url(r'^gerar_ar_inf3/(?P<pk>[0-9]+)', gerar_ar_inf3, name='gerar_ar_inf3'),
    url(r'^editar_infracao/(?P<pk>[0-9]+)', editar_infracao, name='editar_infracao'),
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
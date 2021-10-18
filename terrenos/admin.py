from django.contrib import admin
from .models import Protocolo, Inspecao, Fiscal, Infracao, Notificacao, Terreno, Proprietario
admin.site.register(Protocolo)
admin.site.register(Inspecao)
admin.site.register(Fiscal)
admin.site.register(Infracao)
admin.site.register(Notificacao)
admin.site.register(Terreno)
admin.site.register(Proprietario)
# Register your models here.

from django.db import models

# Create your models here.


class Fiscal(models.Model):
    nome_fiscal = models.CharField(max_length=36, null=False)

    matricula_fiscal = models.CharField(max_length=5, null=False)
    NIVEL_CHOICES = (
        ("FISCAL SANITÁRIO I", "FISCAL SANITÁRIO I"),
        ("FISCAL SANITÁRIO II", "FISCAL SANITÁRIO II"),
    )

    nivel = models.CharField(max_length=19, null=False, choices=NIVEL_CHOICES)

    primeiro_nome = models.CharField(max_length=16, null=False)

    def __str__(self):
        return self.primeiro_nome

    def save(self, *args, **kwargs):
        self.nome_fiscal = self.nome_fiscal.upper()
        self.primeiro_nome = self.primeiro_nome.upper()

        super(Fiscal, self).save(*args, **kwargs)


class Proprietario(models.Model):
    nome_proprietario = models.CharField(max_length=55)
    logradouro_proprietario = models.CharField(max_length=60, null=False)
    numero_proprietario = models.CharField(max_length=10, null=False)
    complemento_proprietario = models.CharField(max_length=30, null=True)
    bairro_proprietario = models.CharField(max_length=30, null=False)
    cep_proprietario = models.CharField(max_length=9, null=False)
    municipio_proprietario = models.CharField(max_length=60, null=False)
    estado_proprietario = models.CharField(max_length=60, null=False)

    #def __str__(self):
     #   return self.nome_proprietario

    def __str__(self):
        return "{}. {}, {} {} - {} ".format(self.nome_proprietario, self.logradouro_proprietario,
                                            self.numero_proprietario, self.complemento_proprietario,self.bairro_proprietario)

    def save(self, *args, **kwargs):
        self.nome_proprietario = self.nome_proprietario.upper()
        self.logradouro_proprietario = self.logradouro_proprietario.upper()
        self.numero_proprietario = self.numero_proprietario.upper()
        self.complemento_proprietario = self.complemento_proprietario.upper()
        self.bairro_proprietario = self.bairro_proprietario.upper()
        self.municipio_proprietario = self.municipio_proprietario.upper()
        self.estado_proprietario = self.estado_proprietario.upper()

        super(Proprietario, self).save(*args, **kwargs)


class Terreno(models.Model):
    inscricao_terreno = models.CharField(max_length=18, null=False, verbose_name="Inscrição imobiliária do terreno")
    logradouro_terreno = models.CharField(max_length=60, null=False, verbose_name="Logradouro do terreno")
    numero_terreno = models.CharField(max_length=10, null=False, verbose_name="Número")
    bairro_terreno = models.CharField(max_length=30, null=False, verbose_name="Bairro")
    CEP_CHOICES = (
        ("37950-000", "37950-000"),
        )
    MUNICIPIO_CHOICES = (
        ("SÃO SEBASTIÃO DO PARAÍSO", "SÃO SEBASTIÃO DO PARAÍSO"),
    )
    ESTADO_CHOICES = (
        ("MINAS GERAIS", "MINAS GERAIS"),
    )
    cep_terreno = models.CharField(max_length=9, null=False, choices=CEP_CHOICES, verbose_name="CEP")
    municipio_terreno = models.CharField(max_length=60, null=False, choices=MUNICIPIO_CHOICES, verbose_name="Cidade")
    estado_terreno = models.CharField(max_length=30, null=False, choices=ESTADO_CHOICES, verbose_name="Estado")
    proprietario = models.ForeignKey('Proprietario', on_delete=models.CASCADE, null=False)
    lote_terreno = models.CharField(max_length=4, null=False)
    quadra_terreno = models.CharField(max_length=4, null=False)
    area_terreno = models.FloatField(null=False)
    logradouro_correspondencia = models.CharField(max_length=60, null=False, verbose_name="Logradouro de correspondência")
    numero_correspondencia = models.CharField(max_length=10, null=False, verbose_name="Número")
    complemento_correspondencia = models.CharField(max_length=30, null=True, verbose_name="Complemento")
    bairro_correspondencia = models.CharField(max_length=30, null=False, verbose_name="Bairro")
    cep_correspondencia = models.CharField(max_length=9, null=False, verbose_name="CEP")
    municipio_correspondencia = models.CharField(max_length=60, null=False, verbose_name="Cidade")
    estado_correspondencia = models.CharField(max_length=30, null=False, verbose_name="Estado")

    #def __str__(self):
        #return self.inscricao_terreno
    def __str__(self):
        return "{} - {}".format(self.inscricao_terreno, self.proprietario)

    # para chamar dois atributos:
    #     def __str__(self):
    #         return "{} ({})".format(self.protocolo, self.protocolo.status_protocolo)
    # porém no return do protocolo tem que estar:
    # return "{} ({})".format(self.protocolo, self.status_protocolo)



    def save(self, *args, **kwargs):
        self.logradouro_terreno = self.logradouro_terreno.upper()
        self.bairro_terreno = self.bairro_terreno.upper()
        self.logradouro_correspondencia = self.logradouro_correspondencia.upper()
        self.bairro_correspondencia = self.bairro_correspondencia.upper()
        self.municipio_correspondencia = self.municipio_correspondencia.upper()
        self.estado_correspondencia = self.estado_correspondencia.upper()

        super(Terreno, self).save(*args, **kwargs)


class Protocolo(models.Model):
    protocolo = models.CharField(max_length=12, null=False)
    SOLICITANTE_CHOICES = (
        ("PESSOA FÍSICA", "PESSOA FÍSICA"),
        ("CORPO DE BOMBEIROS", "CORPO DE BOMBEIROS"),
        ("VEREADORES", "VEREADORES"),
        ("MINISTÉRIO PÚBLICO", "MINISTÉRIO PÚBLICO"),
        ("ORDEM JUDICIAL", "ORDEM JUDICIAL"),
        ("OUTRAS INSTITUIÇÕES", "OUTRAS INSTITUIÇÕES"),
    )
    solicitante_protocolo = models.CharField(max_length=40, null=False, choices=SOLICITANTE_CHOICES)
    logradouro_protocolo = models.CharField(max_length=60, null=False)
    bairro_protocolo = models.CharField(max_length=60, null=False)
    descricao_protocolo = models.CharField(max_length=250, null=False)
    STATUS_CHOICES = (
        ("PENDENTE", "PENDENTE"),
        ("NOTIFICADO", "NOTIFICADO"),
        ("AUTUADO", "AUTUADO"),
        ("DEFESA", "DEFESA"),
        ("ENCERRADO", "ENCERRADO"),
    )
    status_protocolo = models.CharField(max_length=15, null=False, choices=STATUS_CHOICES)
    entrada_protocolo = models.DateField(null=False)
    encerramento_protocolo = models.DateField(null=True)
    fiscal = models.ForeignKey('Fiscal', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.protocolo

    def save(self, *args, **kwargs):
        self.protocolo = self.protocolo.upper()
        self.logradouro_protocolo = self.logradouro_protocolo.upper()
        self.bairro_protocolo = self.bairro_protocolo.upper()
        self.descricao_protocolo = self.descricao_protocolo.upper()

        super(Protocolo, self).save(*args, **kwargs)

class Notificacao(models.Model):
    protocolo = models.ForeignKey('Protocolo', on_delete=models.CASCADE, null=False)
    terreno = models.ForeignKey('Terreno', on_delete=models.CASCADE, null=False)
    data_notificacao = models.DateField(null=False)
    data_inspecao = models.DateField(null=False)
    horario_inspecao = models.TimeField(null=False)
    fiscal = models.ForeignKey('Fiscal', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.id

# para chamar dois atributos:
#     def __str__(self):
#         return "{} ({})".format(self.protocolo, self.protocolo.status_protocolo)
#porém no return do protocolo tem que estar:
# return "{} ({})".format(self.protocolo, self.status_protocolo)

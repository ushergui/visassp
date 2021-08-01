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


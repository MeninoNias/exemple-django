from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Pessoa(models.Model):
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    nome = models.CharField("Nome", max_length=255, null=True, blank=True)
    idade = models.PositiveIntegerField("Idade", validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.nome

class Trabalhador(models.Model):
    class Meta:
        verbose_name = "Trabalhador"
        verbose_name_plural = "Trabalhadores"

    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE, related_name="trabalhadores")

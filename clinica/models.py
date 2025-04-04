from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from datetime import timezone
from django.core.exceptions import ValidationError

especialidade = [
    ("P", "Psiquiatra"),
    ("U", "Urologista"),
    ("O", "Oftalmologista")
]

status = [
    ("A", "Agendado"),
    ("R", "Realizado"),
    ("C", "Cancelado")
]

class Medico(models.Model):
    nome = models.CharField(max_length=50, validators=[
        MinLengthValidator(5)
    ])
    especialidade = models.CharField(max_length=1, choices=especialidade)
    crm = models.CharField(
        max_length=7,
        unique=True,
        validators=[
            MinLengthValidator(7),
            RegexValidator(
                regex='^\d{7}$',
                message='CRM deve conter exatamente 7 dígitos numéricos'
            )
        ],
        help_text="Digite apenas números (7 dígitos)"
    )
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - CRM: {self.crm}"

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

class Consulta(models.Model):
    paciente = models.CharField(max_length=60)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status)
        

from django.db import models
import uuid
import os

TYPE_CHOICES = (
    (1, "Débito"),
    (2, "Boleto"),
    (3, "Financiamento"),
    (4, "Crédito"),
    (5, "Recebimento Empréstimo"),
    (6, "Vendas"),
    (7, "Recebimento TED"),
    (8, "Recebimento DOC"),
    (9, "Aluguel"),
)


class TransactionFIles(models.Model):
    upload = models.FileField(upload_to="transactions/uploads/")

    def filename(self):
        return self.upload.name


class Transactions(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # type = models.CharField(max_length=1)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=1)
    date = models.DateField()
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    credit_card = models.CharField(max_length=12)
    attendance_hour = models.TimeField()
    shop_owner = models.CharField(max_length=14)
    shop_name = models.CharField(max_length=19)

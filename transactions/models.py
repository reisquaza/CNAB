from django.db import models


class Transactions(models.Models):
    type = models.CharField()
    date = models.CharField()
    value = models.CharField()
    cpf = models.CharField()
    credit_card = models.CharField()
    attendance_hour = models.CharField()
    shop_owner = models.CharField()
    shop_name = models.CharField()

from rest_framework.serializers import ModelSerializer
from .models import Transactions

class TransactionnsSerializer(ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"

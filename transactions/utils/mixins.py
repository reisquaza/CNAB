from transactions.forms import UploadTransactionFileForm
from django.shortcuts import render


class TransactionMixin:
    def home_view(request):
        context = {}
        context["form"] = UploadTransactionFileForm()
        return render(request, "home.html", context)

    # def create(self, request, *args, **kwargs):
    #     ...

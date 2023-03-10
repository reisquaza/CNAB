from django.shortcuts import render
from .forms import UploadTransactionFileForm
from .models import TransactionFIles, Transactions
from .serializers import TransactionnsSerializer
from .utils.mixins import TransactionMixin
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView, Response, status
from django.http import HttpResponseRedirect
import os
import ipdb


def home_view(request):
    context = {}

    if request.POST:
        form = UploadTransactionFileForm(request.POST, request.FILES)

        if form.is_valid():
            file_upload = request.FILES["transaction_file"].read()
            file_text = file_upload.decode("UTF-8")
            file_arr = file_text.split("\n")
            # ipdb.set_trace()

            # for line in file_arr:
            #     ipdb.set_trace()

            data = []

            for line in file_arr:
                obj = {
                    "type": line[0],
                    "date": f"{line[1:5]}-{line[5:7]}-{line[7:9]}",
                    "value": line[9:19],
                    "cpf": line[19:30],
                    "credit_card": line[30:42],
                    "attendance_hour": f"{line[42:44]}:{line[44:46]}:{line[46:48]}",
                    "shop_owner": line[48:62],
                    "shop_name": line[62:80],
                }
                data.append(obj)

            # ipdb.set_trace()
            serializer = TransactionnsSerializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            context["data"] = data

            return render(request, "table.html", context)

        else:
            form = UploadTransactionFileForm()

            context["form"] = form
            return render(request, "home.html", context)

    context["form"] = UploadTransactionFileForm()
    return render(request, "home.html", context)


# def home_view(request):
#     context = {}

#     if request.POST:
#         form = UploadTransactionFileForm(request.POST, request.FILES)

#         if form.is_valid():
#             upload = request.FILES["transaction_file"]

#             teste = TransactionFIles(upload=upload)
#             teste.save()

#             ipdb.set_trace()
#         else:
#             form = UploadTransactionFileForm()

#             context["form"] = form
#             return render(request, "home.html", context)

#     context["form"] = UploadTransactionFileForm()
#     return render(request, "home.html", context)


class TransactionsView(APIView):
    def post(self, request):

        upload_file = request.FILES["transaction_file"].read()
        upload_txt = upload_file.decode("UTF-8")
        upload_arr = upload_txt.split("\n")

        for i in upload_arr:
            obj = {
                "type": i[0],
                "date": f"{i[1:5]} - {i[5:7]} - {i[7:9]}",
                "value": int(i[9:17].i[17:19]),
                "cpf": i[19:30],
                "credit_card": i[30:42],
                "hour": f"{i[42:44]:{i[44:46]:i[46:48]}}",
                "shop_owner": i[48:62],
                "shop_name": i[62:80],
            }

        serializer = TransactionnsSerializer(data=obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status.HTTP_201_CREATED)

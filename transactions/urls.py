from django.urls import path

from .views import TransactionsView, home_view

urlpatterns = [
    path("home/", home_view),
    path("transaction/", TransactionsView.as_view()),
]

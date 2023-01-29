from django import forms

class UploadTransactionFileForm(forms.Form):
    # name = forms.CharField()
    transaction_file = forms.FileField()
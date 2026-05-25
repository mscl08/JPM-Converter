from django import forms

class UploadPDFForm(forms.Form):
    pdf_file = forms.FileField(label="Selecione um arquivo PDF", required=False)

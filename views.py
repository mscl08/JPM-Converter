from django.shortcuts import render
from django.http import HttpResponse
from pypdf import PdfReader
import forms
import os  # para manipular nomes de arquivos

def home(request):
    form = forms.UploadPDFForm()
    texto_completo = ""

    if request.method == 'POST':
        if request.FILES.get('pdf_file'):
            arquivo_pdf = request.FILES['pdf_file']
            try:
                leitor = PdfReader(arquivo_pdf)
                for pagina in leitor.pages:
                    texto = pagina.extract_text()
                    if texto:
                        texto_completo += texto + "\n"

                # Pega o nome original e troca a extensão para .txt
                nome_original = os.path.splitext(arquivo_pdf.name)[0]
                nome_txt = f"{nome_original}.txt"

                # Retorna o arquivo para download com o mesmo nome
                response = HttpResponse(texto_completo, content_type="text/plain")
                response["Content-Disposition"] = f'attachment; filename="{nome_txt}"'
                return response

            except Exception as e:
                texto_completo = f"Erro no upload: {e}"
        else:
            texto_completo = "Nenhum arquivo enviado."

    return render(request, 'upload.html', {
        'form': form,
        'texto_extraido': texto_completo
    })

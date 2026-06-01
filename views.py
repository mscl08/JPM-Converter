from django.shortcuts import render
from django.http import HttpResponse
from pypdf import PdfReader
import forms  
from models import RoteiroExtraido  # <-- ADICIONADO: Importando a tabela do banco

def home(request):
    form = forms.UploadPDFForm()  
    texto_completo = ""

    if request.method == 'POST':
        # Tratamento seguro caso você use o formulário web futuramente
        if request.FILES.get('pdf_file'):
            arquivo_pdf = request.FILES['pdf_file']
            try:
                leitor = PdfReader(arquivo_pdf)
                for pagina in leitor.pages:
                    texto = pagina.extract_text()
                    if texto:
                        texto_completo += texto + "\n"
                
                # <-- ADICIONADO: Salva o texto do upload no banco de dados
                if texto_completo.strip():
                    RoteiroExtraido.objects.create(conteudo=texto_completo)
                
                texto_completo = "Sucesso"
            except Exception as e:
                texto_completo = f"Erro no upload: {e}"
        else:
            # Lógica para processar o seu PDF local fixo se clicar no botão
            caminho_pdf = 'C:/Users/xadre/Downloads/ROTEIRO - ACBV CULT 2024.pdf'
            caminho_txt = 'C:/Users/xadre/hello/texto_extraido.txt'
            
            try:
                leitor = PdfReader(caminho_pdf)
                for pagina in leitor.pages:
                    texto = pagina.extract_text()
                    if texto:
                        texto_completo += texto + "\n"
                        
                # <-- ADICIONADO: Salva o texto do PDF fixo local no banco de dados
                if texto_completo.strip():
                    RoteiroExtraido.objects.create(conteudo=texto_completo)

                with open(caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                    arquivo_txt.write(texto_completo)
                
                texto_completo = "Sucesso"
            except Exception as e:
                texto_completo = f"Erro local: {e}"

    return render(request, 'upload.html', {
        'form': form,
        'texto_extraido': texto_completo
    })

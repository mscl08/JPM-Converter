import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracao_site.settings')
django.setup()

# Importa o modelo Documento que acabamos de criar
from models import Documento

def importar_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        
        for linha in linhas:
            linha_limpa = linha.strip()
            if linha_limpa:
                # Salva o texto no campo 'conteudo' do modelo Documento
                Documento.objects.create(conteudo=linha_limpa)
                print(f"Dado salvo: {linha_limpa}")

if __name__ == '__main__':
    arquivo_txt = 'texto_extraido.txt'
    importar_dados(arquivo_txt)

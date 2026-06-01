from django.db import models

class RoteiroExtraido(models.Model):
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Força o Django a reconhecer o modelo mesmo estando fora de um app comum
        app_label = 'configuracao_site'

    def __str__(self):
        return f"Roteiro #{self.id} - {self.criado_em.strftime('%d/%m/%Y %H:%M')}"

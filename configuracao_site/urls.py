from django.contrib import admin
from django.urls import path
import views  # Importa o arquivo views diretamente, sem o ponto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Conecta a página inicial direto na sua função home
]

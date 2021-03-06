"""assinaturaEmail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Apps.assinaturas.views import *

urlpatterns = [
    path('', index, name='index_assinatura'),
    path('criar/assinatura', criar_assinatura, name='criar_assinatura'),
    path('visualizar/assinatura', visualizar_assinatura, name='visualizar_assinatura'),
    path('pesquisar/assinatura/', pesquisar_assinatura, name='pesquisar_assinatura'),
    path('guia/zimbra', guia_zimbra, name='guia_zimbra'),
    path('guia/thunderbird', guia_thunderbird, name='guia_thunderbird'),
    path('guia/outlook', guia_outlook, name='guia_outlook')
]

"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from totem.views import (delete_contato, index_contato, index_criacao,
                         index_agenda, update_contato)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_agenda, name="index"),
    path('criar/', index_criacao, name = "index_criacao"),
    path('contato/<int:id_contato>', index_contato, name="index_contato"),
    path('update/<int:id_contato>', update_contato, name="update_contato"),
    path('delete/<int:id_contato>', delete_contato, name="delete_contato"),
]

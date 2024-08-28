"""cpingfolder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from cpunca import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admncpunca24/', admin.site.urls),
    path('', views.raiz),
    path('tabla_posiciones_copa_unca/', views.tabla_posiciones_unca, name='tabla_posiciones'),
    path('resultados_copa_unca/', views.mostrar_partidos_unca, name='partidos'),
    path('resultados_copa_unca/<int:pk>/', views.resumen_unca, name='resumen'),
    path('copa_unca/', views.deportes_unca),
    path('campeones_copa_unca/', views.tabla_campeones_unca),
    path('100m/', views.cienmetros),
    path('200m/', views.doscientosmetros),
    path('4x100/', views.cuatrocientosmetros),
    path('disco/', views.disco),
    path('bala/', views.bala),
    path('jabalina/', views.jabalina),
    path('saltolargo/', views.saltolargo),
    path('saltotriple/', views.saltotriple),
    path('ciclismo/', views.ciclismo),
    path('tabla_atletismo/', views.tabla_atletismo),
    path ('noticias', views.blog),
    path ('noticias/<slug:pk>', views.single_blog, name='single_blog'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


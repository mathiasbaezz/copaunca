
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import random
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, 'copaunca.html' , {'posts':posts})

def raiz(request):
    return redirect('/copa_unca')

def tabla_posiciones_unca(request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    equipos = EquipoUnca.objects.all()

    # Crear o actualizar las posiciones para cada equipo
    for equipo in equipos:
        posicion, created = PosicionUnca.objects.get_or_create(equipo=equipo)
        # Calcula los puntos totales para cada deporte y género
        puntos_totales = (
            posicion.puntos_futbol_fem +
            posicion.puntos_futbol_masc +
            posicion.puntos_futsal_fem +
            posicion.puntos_futsal_masc +
            posicion.puntos_handball_fem +
            posicion.puntos_handball_masc +
            posicion.puntos_volley_fem +
            posicion.puntos_volley_masc +
            posicion.puntos_basket_fem +
            posicion.puntos_basket_masc +
            posicion.puntos_futbol_universitario +
            posicion.puntos_piki +
            posicion.puntos_ajedrez +
            posicion.puntos_pingpong +
            posicion.puntos_ciclismofem +
            posicion.puntos_ciclismomasc+
            posicion.puntos_atletismo
        )
        # Actualiza los puntos en la posición del equipo
        posicion.puntos = puntos_totales
        posicion.save()

    # Obtén todas las posiciones ordenadas por puntaje total (de mayor a menor)
    posiciones = PosicionUnca.objects.order_by('-puntos')

    return render(request, 'tabla_posicionesunca.html', {'posiciones': posiciones, 'posts':posts })

def tabla_campeones_unca(request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    equipos = EquipoUnca.objects.all()
    champions = ChampionUnca.objects.all()

    # Crear o actualizar las posiciones para cada equipo
    for equipo in equipos:
        campeon, created = CampeonUnca.objects.get_or_create(equipo=equipo)
        # Calcula los puntos totales para cada deporte y género
        total_campeonatos = (
            campeon.campeon_2016 +
            campeon.campeon_2017 +
            campeon.campeon_2018 +
            campeon.campeon_2019 +
            campeon.campeon_2022 +
            campeon.campeon_2023
        )
        # Actualiza los puntos en la posición del equipo
        campeon.total_campeonatos = total_campeonatos
        campeon.save()

    # Obtén todas las posiciones ordenadas por puntaje total (de mayor a menor)
    campeones = CampeonUnca.objects.order_by('-total_campeonatos')

    return render(request, 'tabla_campeonesunca.html', {'posts':posts, 'campeones': campeones, 'champions': champions})

def mostrar_partidos_unca(request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    deporte = request.GET.get('deporte', 'FUTBOL_FEMENINO')  # Valor por defecto: Fútbol Masculino
    partidos = PartidoUnca.objects.filter(deporte=deporte).order_by('-id')
    return render(request, 'partidosunca.html', {'partidouncas': partidos, 'posts':posts})




def resumen_unca(request, pk):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    partido = get_object_or_404(PartidoUnca, pk=pk)
    partidos = PartidoUnca.objects.all()
    eventos_partido = EventoPartidoUnca.objects.filter(partido=partido)
    eventos = EventosUnca.objects.filter(partido=partido)

    context = {
        'partidounca': partido,
        'partidos': partidos,
        'eventos_partido': eventos_partido,
        'eventos': eventos,
        'posts': posts
    }

    return render(request, 'resumenunca.html', context )


def deportes_unca (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    deportes = DeporteUnca.objects.all()
    return render(request, 'copaunca.html', {"posts": posts, "deportes":deportes})


def champions_unca (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    champions = ChampionUnca.objects.all()
    championsgral = ChampiongralUnca.objects.all()
    return render(request, 'tabla_campeonesunca.html', {'posts':posts, "champions":champions, "championsgral":championsgral})

def cienmetros (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, '100m.html' , {'posts':posts})

def doscientosmetros (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, '200m.html' , {'posts':posts})

def cuatrocientosmetros (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, '4x100m.html' , {'posts':posts})

def disco (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, 'disco.html' , {'posts':posts})

def bala (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, 'bala.html' , {'posts':posts})

def jabalina (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, 'jabalina.html' , {'posts':posts})

def saltolargo (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, 'saltolargo.html' , {'posts':posts})

def saltotriple (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, 'saltotriple.html' , {'posts':posts})

def ciclismo (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, 'ciclismo.html' , {'posts':posts})

def tabla_atletismo (request):
    posts = Post.objects.all().order_by('-published_date')[0:4]
    return render(request, 'tabla_atletismo.html' , {'posts':posts})

def blog (request):
    posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paginator_posts = paginator.get_page(page)
    posts = Post.objects.all().order_by('-published_date')[0:6]
    contexto = {"posts_pagin": paginator_posts, "posts": posts}
    return render(request, 'blog.html', contexto)

def single_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all().order_by('-published_date')[0:6]
    contexto = {"post": post, "posts":posts}
    return render(request, 'single_blog.html', contexto)
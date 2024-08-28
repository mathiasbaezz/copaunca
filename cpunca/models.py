from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class EquipoUnca(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class PartidoUnca(models.Model):
    DEPORTE_CHOICES = (
        ('FUTBOL_FEMENINO', 'Fútbol de Campo Femenino'),
        ('FUTBOL_MASCULINO', 'Fútbol de Campo Masculino'),
        ('FUTSAL_FEMENINO', 'Fútsal Femenino'),
        ('FUTSAL_MASCULINO', 'Fútsal Masculino'),
        ('HANDBALL_FEMENINO', 'Handball Femenino'),
        ('HANDBALL_MASCULINO', 'Handball Masculino'),
        ('VOLLEY_FEMENINO', 'Volley Femenino'),
        ('VOLLEY_MASCULINO', 'Volley Masculino'),
        ('BASKET_FEMENINO', 'Básquet Femenino'),
        ('BASKET_MASCULINO', 'Básquet Masculino'),
        ('FUTBOL_UNIVERSITARIO', 'Fútbol Universitario'),
        ('PIKI', 'Piki'),
        ('AJEDREZ', 'Ajedrez'),
        ('PING_PONG', 'Ping Pong'),
    )


    equipo_local = models.ForeignKey(EquipoUnca, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(EquipoUnca, on_delete=models.CASCADE, related_name='partidos_visitante')
    goles_local = models.PositiveIntegerField(blank=True, null=True)
    goles_visitante = models.PositiveIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    partido_numero = models.CharField(max_length=100, blank=True, null=True)
    fase_partido = models.CharField(max_length=99, blank=True, null=True)
    deporte = models.CharField(max_length=50, choices=DEPORTE_CHOICES, blank=True, null=True)


    def __str__(self):
        return f"PartidoUnca {self.id} {self.equipo_local} vs {self.equipo_visitante}"

    def get_absolute_url(self):
        return reverse('resumen_unca', kwargs={'pk': self.pk})


class EventoPartidoUnca(models.Model):
    PARTIDO_EVENT_CHOICES = (
        ('INICIO DEL PARTIDO', 'Inicio del partido'),
        ('PENDIENTE', 'Pendiente'),
        ('FINAL DEL PARTIDO', 'Fin del partido'),
    )

    partido = models.ForeignKey(PartidoUnca, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100, choices=PARTIDO_EVENT_CHOICES)
    minuto = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} en el minuto {self.minuto} del partido {self.partido}"


class EventosUnca(models.Model):
    PARTIDO_EVENT_CHOICES = (
        ('GOOOOL', 'Gol local'),
        ('GOOOL', 'Gol visitante'),
        ('PUNTO', 'Punto local'),
        ('PUNTO ', 'Punto visitante'),
        ('TARJETA ROJA', 'Tarjeta roja local'),
        ('TARJETA ROJA ', 'Tarjeta roja visitante'),
        ('TARJETA AMARILLA', 'Tarjeta amarilla local'),
        ('TARJETA AMARILLA ', 'Tarjeta amarilla visitante'),
    )

    partido = models.ForeignKey(PartidoUnca, on_delete=models.CASCADE)
    minuto = models.PositiveIntegerField()
    tipo = models.CharField(max_length=100, choices=PARTIDO_EVENT_CHOICES)
    jugadores = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.tipo} en el minuto {self.minuto} del partido {self.partido}"

from django.db import models

class PosicionUnca(models.Model):
    equipo = models.ForeignKey(EquipoUnca, on_delete=models.CASCADE)
    puntos_futbol_fem = models.IntegerField(default=0)
    puntos_futbol_masc = models.IntegerField(default=0)
    puntos_futsal_fem = models.IntegerField(default=0)
    puntos_futsal_masc = models.IntegerField(default=0)
    puntos_handball_fem = models.IntegerField(default=0)
    puntos_handball_masc = models.IntegerField(default=0)
    puntos_volley_fem = models.IntegerField(default=0)
    puntos_volley_masc = models.IntegerField(default=0)
    puntos_basket_fem = models.IntegerField(default=0)
    puntos_basket_masc = models.IntegerField(default=0)
    puntos_futbol_universitario = models.IntegerField(default=0)
    puntos_piki = models.IntegerField(default=0)
    puntos_ajedrez = models.IntegerField(default=0)
    puntos_pingpong = models.IntegerField(default=0)
    puntos_ciclismofem = models.IntegerField(default=0)
    puntos_ciclismomasc = models.IntegerField(default=0)
    puntos_atletismo = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.equipo}"


class CampeonUnca(models.Model):
    equipo = models.ForeignKey(EquipoUnca, on_delete=models.CASCADE)
    campeon_2016 = models.IntegerField(default=0,)
    campeon_2017 = models.IntegerField(default=0)
    campeon_2018 = models.IntegerField(default=0)
    campeon_2019 = models.IntegerField(default=0)
    campeon_2022 = models.IntegerField(default=0)
    campeon_2023 = models.IntegerField(default=0)
    total_campeonatos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.equipo}"

class TablaPosicionesUnca(models.Model):
    equipo = models.ForeignKey(EquipoUnca, on_delete=models.CASCADE)
    puntos = models.PositiveIntegerField(default=0)
    partidos_jugados = models.PositiveIntegerField(default=0)
    partidos_ganados = models.PositiveIntegerField(default=0)
    partidos_empatados = models.PositiveIntegerField(default=0)
    partidos_perdidos = models.PositiveIntegerField(default=0)
    goles_favor = models.PositiveIntegerField(default=0)
    goles_contra = models.PositiveIntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)
    @staticmethod
    def calcular_posiciones():
        equipos = EquipoUnca.objects.all()
        TablaPosicionesUnca.objects.all().delete()
        for equipo in equipos:
            partidos_local = PartidoUnca.objects.filter(equipo_local=equipo)
            partidos_visitante = PartidoUnca.objects.filter(equipo_visitante=equipo)
            partidos_jugados = partidos_local.count() + partidos_visitante.count()
            partidos_ganados = partidos_local.filter(goles_local__gt=models.F('goles_visitante')).count()
            partidos_ganados += partidos_visitante.filter(goles_visitante__gt=models.F('goles_local')).count()
            partidos_empatados = partidos_local.filter(goles_local=models.F('goles_visitante')).count()
            partidos_empatados += partidos_visitante.filter(goles_visitante=models.F('goles_local')).count()
            partidos_perdidos = partidos_jugados - partidos_ganados - partidos_empatados
            goles_favor = partidos_local.aggregate(total=models.Sum('goles_local'))['total'] or 0
            goles_favor += partidos_visitante.aggregate(total=models.Sum('goles_visitante'))['total'] or 0
            goles_contra = partidos_local.aggregate(total=models.Sum('goles_visitante'))['total'] or 0
            goles_contra += partidos_visitante.aggregate(total=models.Sum('goles_local'))['total'] or 0
            puntos = partidos_ganados * 3 + partidos_empatados
            diferencia_goles = goles_favor - goles_contra
            TablaPosicionesUnca.objects.create(
                equipo=equipo,
                puntos=puntos,
                partidos_jugados=partidos_jugados,
                partidos_ganados=partidos_ganados,
                partidos_empatados=partidos_empatados,
                partidos_perdidos=partidos_perdidos,
                goles_favor=goles_favor,
                goles_contra=goles_contra,
                diferencia_goles=diferencia_goles
            )
@receiver(post_save, sender=PartidoUnca)
def actualizar_tabla_posiciones(sender, instance, **kwargs):
    TablaPosicionesUnca.calcular_posiciones()


class DeporteUnca(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class ChampionUnca(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)
    link = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.nombre

class ChampiongralUnca(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)
    link = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.nombre


class Categoria1 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre


class Categoria2 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre

class Categoria3 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    categoria1 = models.ForeignKey('Categoria1', on_delete=models.CASCADE,null=True)
    categoria2 = models.ForeignKey ('Categoria2', on_delete=models.CASCADE, null=True)
    categoria3 = models.ForeignKey('Categoria3', on_delete=models.CASCADE, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    slug= models.SlugField(null=False, default="#")

    def get_absolute_url(self):
        return reverse('single_blog', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

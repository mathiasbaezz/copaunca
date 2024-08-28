from django.contrib import admin
from .models import *
# Register your models here.

class EventoPartidoUncaInline(admin.TabularInline):
    model = EventoPartidoUnca
    extra = 1

class EventosUncaInline(admin.TabularInline):
    model = EventosUnca
    extra = 1

class PartidoUncaAdmin(admin.ModelAdmin):
    list_display = ['equipo_local', 'equipo_visitante', 'fecha', 'deporte', 'fase_partido']
    inlines = [EventoPartidoUncaInline, EventosUncaInline]

admin.site.register(EquipoUnca)
admin.site.register(PartidoUnca, PartidoUncaAdmin)
admin.site.register(EventoPartidoUnca)
admin.site.register(EventosUnca)
admin.site.register(TablaPosicionesUnca)
admin.site.register(PosicionUnca)
admin.site.register(CampeonUnca)
admin.site.register(DeporteUnca)
admin.site.register(ChampionUnca)
admin.site.register(ChampiongralUnca)
admin.site.register(Categoria1)
admin.site.register(Categoria2)
admin.site.register(Categoria3)
admin.site.register(Post)


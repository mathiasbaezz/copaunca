from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Partido, TablaPosiciones

@receiver(post_save, sender=Partido)
def actualizar_tabla_posiciones(sender, instance, **kwargs):
    TablaPosiciones.calcular_posiciones()

from django.db import models
from ligapp.models import Equipo, Jugador

# Create your models here.

class Jornada(models.Model):
	numero=models.IntegerField(default=0)
	def __unicode__(self):
		return unicode (self.numero)

class Partido(models.Model):
	equipoLocal=models.ForeignKey(Equipo,related_name='local')
	equipoVisit=models.ForeignKey(Equipo,related_name='visitante')
	fechaInicio=models.DateTimeField()
	resultado=models.CharField(max_length=10)
	jornada=models.ForeignKey(Jornada)
	enjuego="En juego"
	noempezado="No empezado"
	finalizado="Finalizado"
	opsituacion=((enjuego, 'En juego'), (noempezado, 'No empezado'), (finalizado, 'Finalizado'))
	situacion=models.CharField(max_length=30, choices=opsituacion)
	def __unicode__(self):
		return self.equipoLocal.nombre+"-"+self.equipoVisit.nombre

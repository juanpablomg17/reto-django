from django.db import models

# Create your models here.

# DESARROLLAR UNA APLICACION WEB DJANGO QUE PERMITE GESTIONAR LAS METRICAS DE SALUD BASICAS, PROVENIENTES DE UN DISPOSITIVO BIOMETRICO(SMARTBAND/SMARTWATCH) REFERENTES A:

# 1. Frecuencia Cardiaca(Heart Rate) medida en BPM(Beats per minute)/Pulsaciones por minuto
# 2. Saturación de Oxígeno en Sangre(SpO2)
# 3. Nivel de Stress

# Las métricas anteriores, deben estar acompañadas con los datos del usuario: Nombres, Apellidos, Edad y Peso.

# El código fuente del proyecto se deberá desplegar en la plataforma GITHUB y suministrar la URL para validarlo


class User(models.Model):
    id: models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    hearRate = models.DecimalField(max_digits=100, decimal_places=4)
    oxygenSaturation = models.DecimalField(max_digits=100, decimal_places=4)
    stressLevel = models.DecimalField(max_digits=100, decimal_places=4)
    
    def __str__(self):
        text =  "{0} {1}"
        return text.format(self.name, self.lastname)
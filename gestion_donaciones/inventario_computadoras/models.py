from django.db import models
from .choices import OpComputadora, OpcionesArquitectura


class Microprocesador(models.Model):
    nombre = models.CharField(max_length=50)
    arquitectura = models.CharField(max_length=3, choices=OpcionesArquitectura.OPCIONES_ARQUITECTURA)

    class Meta:
        verbose_name_plural = "Microprocesadores"

    def __str__(self):
        return self.nombre


class TarjetaMemoriaRam(models.Model):
    tamano = models.IntegerField(help_text="En MB, ejemplo: 512, 1024, 2048")
    fabricante = models.CharField(max_length=10, blank=True)
    tipo = models.CharField(max_length=4, help_text="Ejemplo: DDR2, DDR3, etc.", blank=True)
    velocidad = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name_plural = "Tarjetas de Memoria RAM"

    def __str__(self):
        return f"Memoria Ram {self.fabricante} de {self.tamano} MB"


class DiscoRigido(models.Model):
    tamano = models.IntegerField(help_text="Tamaño en GB, ejemplo: 500, 1000, etc.")
    fabricante = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name_plural = "Discos Rígidos"

    def __str__(self):
        return f"Disco Rigido {self.fabricante} de {self.tamano}"


class SistemaOperativo(models.Model):
    nombre = models.CharField(max_length=25, help_text="Ej: Ubuntu 20.04 LTS")
    arquitectura = models.CharField(max_length=3, choices=OpcionesArquitectura.OPCIONES_ARQUITECTURA)

    class Meta:
        verbose_name_plural = "Sistemas operativos"

    def __str__(self):
        return f"{self.nombre} {self.arquitectura}"


class Computadora(models.Model):
    estado = models.CharField(max_length=12, choices=OpComputadora.OPCIONES_ESTADO)
    formato = models.CharField(max_length=12, choices=OpComputadora.OPCIONES_FORMATO)
    procesador = models.ForeignKey(Microprocesador, on_delete=models.PROTECT, blank=True)
    memoria = models.ForeignKey(TarjetaMemoriaRam, on_delete=models.PROTECT, blank=True)
    disco = models.ForeignKey(DiscoRigido, on_delete=models.PROTECT, blank=True)
    sist_op = models.ForeignKey(SistemaOperativo, on_delete=models.PROTECT, blank=True)
    motherboard = models.CharField(max_length=12, choices=OpComputadora.OPCIONES_FUNCIONAMIENTO, blank=True)
    audio = models.CharField(max_length=12, choices=OpComputadora.OPCIONES_FUNCIONAMIENTO, blank=True)
    fuente = models.CharField(max_length=12, choices=OpComputadora.OPCIONES_FUNCIONAMIENTO, blank=True)
    funcionamiento_red = models.CharField(max_length=12, choices=OpComputadora.OPCIONES_FUNCIONAMIENTO, blank=True)
    cambio_pasta = models.CharField(max_length=2, choices=OpComputadora.OPCION_SI_NO, default=OpComputadora.NO)
    notas = models.CharField(max_length=140, blank=True)

    class Meta:
        verbose_name_plural = "Computadoras"

    def __str__(self):
        return f"Computadora {self.id} - {self.formato}"

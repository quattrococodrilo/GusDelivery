""" 
d_codigo        - Código Postal asentamiento
d_asenta        - Nombre asentamiento
d_tipo_asenta   - Tipo de asentamiento (Catálogo SEPOMEX)
D_mnpio         - Nombre Municipio (INEGI, Marzo 2013)
d_estado        - Nombre  Entidad (INEGI, Marzo 2013)
d_ciudad        - Nombre Ciudad (Catálogo SEPOMEX)
d_CP            - Código Postal de la Administración Postal que reparte al asentamiento
c_estado        - Clave Entidad (INEGI, Marzo 2013)
c_oficina       - Código Postal de la Administración Postal que reparte al asentamiento
c_CP            - Campo Vacio
c_tipo_asenta   - Clave Tipo de asentamiento (Catálogo SEPOMEX)
c_mnpio         - Clave Municipio (INEGI, Marzo 2013)
id_asenta_cpcons - Identificador único del asentamiento (nivel municipal)
d_zona          - Zona en la que se ubica el asentamiento (Urbano/Rural)
c_cve_ciudad    - Clave Ciudad (Catálogo SEPOMEX)
"""

from django.db import models

import unidecode

class Base(models.Model):
    """ Esta clase abstracta es padre de las clases 
    Estado, Municipio y Asentamiento. """

    std_nombre = models.CharField(
        'nombre estandarizado',
        max_length=255,
    )

    def save(self, *args, **kwargs):

        self.std_nombre = unidecode.unidecode(self.std_nombre).lower()

        super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Estado(Base):
    """  """
    d_estado = models.CharField(
        'nombre',
        max_length=255,
        unique=True,
    )

    c_estado = models.CharField(
        'clave',
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.d_estado


class Municipio(Base):
    """  """
    d_mnpio = models.CharField(
        'nombre',
        max_length=255,
    )

    c_mnpio = models.CharField(
        'clave',
        max_length=255,
    )

    d_ciudad = models.CharField(
        'ciudad',
        max_length=255,
        null=True,
        blank=True,
    )

    c_cve_ciudad = models.CharField(
        'ciudad clave',
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.d_mnpio


class Asentamiento(Base):
    """ """
    d_asenta = models.CharField(
        'nombre',
        max_length=255,
    )

    d_tipo_asenta = models.CharField(
        'tipo',
        max_length=255,
    )

    c_tipo_asenta = models.CharField(
        'tipo clave',
        max_length=255,
    )

    id_asenta_cpcons = models.CharField(
        'id nivel municipal',
        max_length=255,
    )

    d_cp = models.CharField(
        'cp administración',
        max_length=255,
    )

    d_oficina = models.CharField(
        'cp oficina',
        max_length=255,
    )

    d_zona = models.CharField(
        'zona',
        max_length=255,
    )

    def __str__(self):
        return self.d_asenta


class CodigoPostal(models.Model):
    """  """
    d_codigo = models.CharField(
        'código postal',
        max_length=255,
    )

    d_estado = models.ForeignKey(
        'Estado',
        verbose_name='estado',
        on_delete=models.CASCADE,
    )

    d_mnpio = models.ForeignKey(
        'Municipio',
        verbose_name='municipio',
        on_delete=models.CASCADE,
    )

    d_asenta = models.ForeignKey(
        'Asentamiento',
        verbose_name='asentamiento',
        on_delete=models.CASCADE,
    )

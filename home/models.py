# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Usuario(models.Model):

    #__Usuario_FIELDS__
    telefono = models.CharField(max_length=255, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=255, null=True, blank=True)

    #__Usuario_FIELDS__END

    class Meta:
        verbose_name        = _("Usuario")
        verbose_name_plural = _("Usuario")


class Estudiante(models.Model):

    #__Estudiante_FIELDS__
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=255, null=True, blank=True)
    semestre = models.IntegerField(null=True, blank=True)

    #__Estudiante_FIELDS__END

    class Meta:
        verbose_name        = _("Estudiante")
        verbose_name_plural = _("Estudiante")



#__MODELS__END

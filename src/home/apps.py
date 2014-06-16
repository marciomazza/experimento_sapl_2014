# -*- coding: utf-8 -*-
from crispy_forms.layout import Submit
from django.apps import AppConfig


class HomeConfig(AppConfig):

    name = 'home'

    def ready(self):
        # Botões de submit mais simples para toda a aplicação
        Submit.field_classes = 'btn btn-default'

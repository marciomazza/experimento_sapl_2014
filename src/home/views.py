# -*- coding: utf-8 -*-
import django.contrib.auth.views
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .areas import areas_em_pares


def index(request):
    """Página Inicial"""

    return render(request, 'home.html', {'areas': areas_em_pares})

def login(request):
    """Página de Login"""

    helper = FormHelper()
    helper.form_id = 'login-form'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-1'
    helper.field_class = 'col-lg-3'
    helper.form_method = 'post'

    login_path = reverse('login')
    helper.form_action = login_path

    next_path = request.REQUEST.get('next', '/')
    if next_path == login_path:
        next_path = '/'
    helper.add_input(Hidden('next', next_path))
    helper.add_input(Submit('submit', 'Submit'))

    return django.contrib.auth.views.login(request, extra_context={'helper': helper})

def logout(request):
    django.contrib.auth.views.logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/'))

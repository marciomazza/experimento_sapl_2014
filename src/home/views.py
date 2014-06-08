# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden
import django.contrib.auth.views
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    """Página Inicial"""

    return render(request, 'home.html')

def login(request):
    """Página de Login"""

    helper = FormHelper()
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

# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
import pytest
from django.test.html import parse_html as html


pytestmark = pytest.mark.django_db

@pytest.fixture
def user():
    return User.objects.create_user('jfirmino', password='123')

def test_login_aparece_na_barra_para_usuario_nao_logado(client, user):
    response = client.get('/')
    assert '<a href="/login/?next=/">Login</a>' in response.content

def test_username_do_usuario_logado_aparece_na_barra(client, user):
    assert client.login(username='jfirmino', password='123')
    response = client.get('/')
    assert html('<a href="/login/?next=/">Login</a>') not in html(response.content)
    assert 'jfirmino' in response.content
    assert html('<a href="/logout/?next=/">Sair</a>') in html(response.content)

def test_nome_completo_do_usuario_logado_aparece_na_barra(client, user):
    # nome completo para o usuario
    user.first_name = 'Joao'
    user.last_name = 'Firmino'
    user.save()
    assert client.login(username='jfirmino', password='123')
    response = client.get('/')
    assert html('<a href="/login/?next=/">Login</a>') not in html(response.content)
    assert 'Joao Firmino' in response.content
    assert html('<a href="/logout/?next=/">Sair</a>') in html(response.content)

def __login(app, uri):
    # estamos na página '/zzzz'
    pagina_login = app.get(uri)
    form = pagina_login.forms['login-form']
    form['username'], form['password'] = 'jfirmino', '123'
    return form.submit()

def test_login_funciona(app, user):
    __login(app, '/login/?next=/zzzz')
    assert user.pk == app.session['_auth_user_id']

def test_login_redireciona_para_origem(app, user):
    res = __login(app, '/login/?next=/zzzz')
    assert res.url == 'http://testserver/zzzz'

def test_login_da_propria_pagina_de_login_redireciona_para_home(app, user):
    # estamos na página '/login' e clicamos no link Login
    res = __login(app, '/login/?next=/login/')
    assert res.url == 'http://testserver/'

def test_login_redireciona_para_home_por_padrao(app, user):
    res = __login(app, '/login/')
    assert res.url == 'http://testserver/'

def __logout(client, uri, user):
    assert client.login(username='jfirmino', password='123')
    # o usuário está logado
    assert user.pk == client.session['_auth_user_id']
    return client.get(uri)

def test_logout_funciona(client, user):
    __logout(client, '/logout/?next=/', user)
    assert '_auth_user_id' not in client.session

def test_logout_redireciona_para_origem(client, user):
    res = __logout(client, '/logout/?next=/zzzz', user)
    assert res.url == 'http://testserver/zzzz'

def test_logout_redireciona_para_home_por_padrao(client, user):
    res = __logout(client, '/logout/', user)
    assert res.url == 'http://testserver/'

# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from django_webtest import WebTest


class ConfiguracaoTestCase(TestCase):

    def test_admin_disponivel(self):
        response = self.client.get('/admin', follow=True)
        self.assertContains(response, 'Admin')


class LoginTestCase(WebTest):

    def setUp(self):
        # usuario sem nome completo
        self.user = User.objects.create_user('jfirmino', password='123')

    def test_login_aparece_na_barra_para_usuario_nao_logado(self):
        response = self.client.get('/')
        self.assertContains(response, '<a href="/login/?next=/">Login</a>')

    def test_username_do_usuario_logado_aparece_na_barra(self):
        self.assertTrue(self.client.login(username='jfirmino', password='123'))
        response = self.client.get('/')
        self.assertNotContains(response, '<a href="/login/?next=/">Login</a>', html=True)
        self.assertContains(response, 'jfirmino')
        self.assertContains(response, '<a href="/logout/?next=/">Sair</a>', html=True)

    def test_nome_completo_do_usuario_logado_aparece_na_barra(self):
        # nome completo para o usuario
        self.user.first_name = 'Joao'
        self.user.last_name = 'Firmino'
        self.user.save()
        self.assertTrue(self.client.login(username='jfirmino', password='123'))
        response = self.client.get('/')
        self.assertNotContains(response, '<a href="/login/?next=/">Login</a>', html=True)
        self.assertContains(response, 'Joao Firmino')
        self.assertContains(response, '<a href="/logout/?next=/">Sair</a>', html=True)

    def do_login_form(self, next):
        # estamos na página '/zzzz'
        pagina_login = self.app.get('/login/?next=' + next)
        form = pagina_login.forms['login-form']
        form['username'], form['password'] = 'jfirmino', '123'
        return form.submit()

    def test_login_acontece(self):
        self.do_login_form(next='/zzzz')
        self.assertEquals(self.user.pk, self.app.session['_auth_user_id'])

    def test_login_redireciona_para_origem(self):
        res = self.do_login_form(next='/zzzz')
        self.assertEquals(res.url, 'http://testserver/zzzz')

    def test_login_da_propria_pagina_de_login_redireciona_para_home(self):
        # estamos na página '/login' e clicamos no link Login
        res = self.do_login_form(next='/login/')
        self.assertEquals(res.url, 'http://testserver/')


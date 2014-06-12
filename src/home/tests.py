from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

class ConfiguracaoTestCase(TestCase):

    def test_admin_disponivel(self):
        c = Client()
        response = c.get('/admin', follow=True)
        self.assertContains(response, 'Admin')

class LoginTestCase(TestCase):

    def test_login_aparece_na_barra_para_usuario_nao_logado(self):
        c = Client()
        response = c.get('/')
        self.assertContains(response, '<a href="/login/?next=/">Login</a>')

    def test_username_do_usuario_logado_aparece_na_barra(self):
        c = Client()
        # usuario sem nome completo
        User.objects.create_user('jfirmino', password='123')
        self.assertTrue(c.login(username='jfirmino', password='123'))
        response = c.get('/')
        self.assertNotContains(response, '<a href="/login/?next=/">Login</a>', html=True)
        self.assertContains(response, 'jfirmino')
        self.assertContains(response, '<a href="/logout/?next=/">Sair</a>', html=True)

    def test_nome_completo_do_usuario_logado_aparece_na_barra(self):
        c = Client()
        # usuario COM nome completo
        User.objects.create_user(username='jfirmino',
                                 password='123',
                                 first_name='Joao',
                                 last_name='Firmino')
        self.assertTrue(c.login(username='jfirmino', password='123'))
        response = c.get('/')
        self.assertNotContains(response, '<a href="/login/?next=/">Login</a>', html=True)
        self.assertContains(response, 'Joao Firmino')
        self.assertContains(response, '<a href="/logout/?next=/">Sair</a>', html=True)

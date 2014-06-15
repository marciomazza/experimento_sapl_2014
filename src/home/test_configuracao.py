# -*- coding: utf-8 -*-

def test_admin_disponivel(client):
    response = client.get('/admin', follow=True)
    assert 'Admin' in response.content

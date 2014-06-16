# -*- coding: utf-8 -*-
from django.utils.text import slugify


TEXTOS = [u"""Mesa Diretora

Órgão colegiado, composto de no mínimo três membros efetivos - Presidente e 1º
e 2º Secretários - a quem cabe a direção dos trabalhos legislativos. Os
parlamentares integrantes da Mesa Diretora são eleitos por seus pares na
primeira reunião de instalação do período legislativo, para um mandato de dois
anos.
""",

u"""Comissões

Órgãos da Casa Legislativa, de natureza técnica especializada e que têm por
objetivo prestar melhores esclarecimentos aos parlamentares para a tomada de
decisões. Assim, as comissões elaboram estudos, pareceres a respeito de
determinados projetos de lei e investigação de irregularidades sobre o fato
determinado.
""",

u"""Parlamentares

O Poder Legislativo, exercido pelo sistema de representação, tem nos
parlamentares a sua expressão máxima. Devem transformar os anseios de seus
representados em ações diretas, na forma de leis ou buscando junto do Executivo
obras e atos que beneficiem a sua comunidade. Possuem funções legisladora,
administrativa, julgadora e de fiscalização sobre a conduta do Executivo.
""",

u"""Ordem do Dia

Utilizada para se determinar quais projetos serão discutidos e votados. A
responsabilidade pela elaboração da Ordem do Dia é definida no Regimento
Interno que, em geral, dá poderes ao Presidente da Casa Legislativa para a sua
elaboração. Também, pode ficar a cargo de um colégio de líderes dos partidos
políticos.
""",

u"""Sessão Plenária

Foro apropriado para a tomada de decisões sobre os projetos de lei e outras
matérias legislativas ou administrativas, aprovadas ou rejeitadas em votação
pelos parlamentares. É dirigida pela Mesa Diretora de acordo com o Regimento
Interno da Casa. As decisões votadas em plenário são soberanas e prevalecem
sobre interesses ou vontades individuais.
""",

u"""Matérias Legislativas

Tem início com o processo de criação de lei e a apresentação de projeto no
Poder Legislativo. Na apreciação de matérias, podem haver eventuais conflitos
de interpretação ou de entendimento entre o que estabelece o Regimento Interno
da Casa e a Lei Orgânica do Município. Nestes casos, prevalece a Lei Orgânica.
""",

u"""Normas Jurídicas

Nos municípios, referem-se as emendas à Lei Orgânica, as leis complementares,
as leis ordinárias, os decretos legislativos e as resoluções.
""",

u"""Relatórios

Contém informações estatísticas sobre a produção legislativa dos parlamentares
e da Casa, dispostas e agrupadas de diferentes formas de acordo com parâmetros
fornecidos.
u"""]

areas = []
for texto in TEXTOS:
    nome, descricao = texto.split('\n\n')
    slug = slugify(nome)
    areas.append({'nome': nome,
                  'caminho': slug,
                  'icone': 'icon-%s.gif' % slug,
                  'descricao': descricao})
areas_em_pares = zip(areas[::2], areas[1::2])

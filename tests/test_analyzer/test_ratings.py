# flake8: noqa

from tech_news.analyzer.ratings import (top_5_news, top_5_categories)
from pymongo import MongoClient
from decouple import config

client = MongoClient(host="mongodb", port=27017)

db = client.tech_news

NEW_NOTICE_1 = {'url': 'https://www.tecmundo.com.br/noticia_1.htm',
                       'title': 'noticia_1',
                       'timestamp': '2020-11-23T11:00:01',
                       'writer': 'Escritor_1',
                       'shares_count': 1,
                       'comments_count': 1,
                       'summary': 'Sumario da noticia_1',
                       'sources': ['Fonte_1'],
                       'categories': ['PC_1', 'Console_1']}

NEW_NOTICE_2 = {'url': 'https://www.tecmundo.com.br/noticia_2.htm',
                       'title': 'noticia_2',
                       'timestamp': '2020-11-23T11:00:01',
                       'writer': 'Escritor_2',
                       'shares_count': 1,
                       'comments_count': 1,
                       'summary': 'Sumario da noticia_2',
                       'sources': ['Fonte_2'],
                       'categories': ['PC_2', 'Console_2']}

NEW_NOTICE_3 = {'url': 'https://www.tecmundo.com.br/noticia_3.htm',
                       'title': 'noticia_3',
                       'timestamp': '2020-11-23T11:00:01',
                       'writer': 'Escritor_3',
                       'shares_count': 1,
                       'comments_count': 1,
                       'summary': 'Sumario da noticia_3',
                       'sources': ['Fonte_3'],
                       'categories': ['PC_3', 'Console_3']}

NEW_NOTICE_4 = {'url': 'https://www.tecmundo.com.br/noticia_4.htm',
                       'title': 'noticia_4',
                       'timestamp': '2020-11-23T11:00:01',
                       'writer': 'Escritor_4',
                       'shares_count': 1,
                       'comments_count': 1,
                       'summary': 'Sumario da noticia_4',
                       'sources': ['Fonte_4'],
                       'categories': ['PC_4', 'Console_4']}

NEW_NOTICE_5 = {'url': 'https://www.tecmundo.com.br/noticia_5.htm',
                       'title': 'noticia_5',
                       'timestamp': '2020-11-23T11:00:01',
                       'writer': 'Escritor_5',
                       'shares_count': 1,
                       'comments_count': 1,
                       'summary': 'Sumario da noticia_5',
                       'sources': ['Fonte_5'],
                       'categories': ['PC_5', 'Console_5']}

NEW_NOTICE_6 = {'url': 'https://www.tecmundo.com.br/noticia_6.htm',
                       'title': 'noticia_6',
                       'timestamp': '2020-11-23T11:00:01',
                       'writer': 'Escritor_6',
                       'shares_count': 1,
                       'comments_count': 1,
                       'summary': 'Sumario da noticia_6',
                       'sources': ['Fonte_6'],
                       'categories': ['PC_6', 'Console_6']}

LIST_FIVE_NOTICES = [('noticia_1',
                      'https://www.tecmundo.com.br/noticia_1.htm'),
                     ('noticia_2',
                      'https://www.tecmundo.com.br/noticia_2.htm'),
                     ('noticia_3',
                      'https://www.tecmundo.com.br/noticia_3.htm'),
                     ('noticia_4',
                      'https://www.tecmundo.com.br/noticia_4.htm'),
                     ('noticia_5',
                      'https://www.tecmundo.com.br/noticia_5.htm')]

LIST_FIVE_CATEGORY = ['Console_1', 'Console_2',
                      'Console_3', 'Console_4',
                      'Console_5']


def test_listar_as_top_cinco_noticias():
    db.news.delete_many({})
    db.news.insert_many([NEW_NOTICE_1, NEW_NOTICE_2, NEW_NOTICE_3,
                         NEW_NOTICE_4, NEW_NOTICE_5, NEW_NOTICE_6])
    assert top_5_news() == LIST_FIVE_NOTICES

def test_buscar_top_noticias_retornar_vazio_caso_nao_exista_noticias():
    db.news.delete_many({})
    assert top_5_news() == []


def test_listar_as_top_cinco_categorias():
    db.news.delete_many({})
    db.news.insert_many([NEW_NOTICE_1, NEW_NOTICE_2, NEW_NOTICE_3,
                         NEW_NOTICE_4, NEW_NOTICE_5, NEW_NOTICE_6])
    assert top_5_categories() == LIST_FIVE_CATEGORY


def test_buscar_top_categorias_retornar_vazio_caso_nao_exista_noticias():
    db.news.delete_many({})
    assert top_5_categories() == []
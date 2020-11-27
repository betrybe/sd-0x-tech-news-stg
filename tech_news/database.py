from pymongo import MongoClient
from decouple import config


client = MongoClient(host="mongodb", port=27017)
db = client.tech_news


def insert_or_update(notice):
    """Seu código deve vir aqui"""


def check_duplicates(news):
    """Seu código deve vir aqui"""

def aggregate_news(query):
    with MongoClient() as client:
        db = client.tech_news
        return list(db.news.aggregate(query))
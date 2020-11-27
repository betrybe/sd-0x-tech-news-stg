# flake8: noqa

from pymongo import MongoClient
from decouple import config

client = MongoClient("mongodb://mongodb:27017/")
db = client.tech_news


def insert_or_update(notice):
    return  db.news.update_one({"url": notice['url']}, {"$set": notice}, upsert=True).upserted_id is not None


def check_duplicates(news):
    """Seu código deve vir aqui"""

def create_news(data):
    with MongoClient() as client:
        db = client.tech_news

        db.news.insert_many(data)

def find_news():
    with MongoClient() as client:
        db = client.tech_news

        return list(db.news.find({}, {'_id': False}))

def search_news(query):
    with MongoClient() as client:
        db = client.tech_news
        return list(db.news.find(query))

def aggregate_news(query):
    with MongoClient() as client:
        db = client.tech_news
        return list(db.news.aggregate(query))
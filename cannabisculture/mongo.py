from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cannabis_culture"]
emails_collection = db["emails"]
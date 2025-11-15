from pymongo import MongoClient

uri = "mongodb+srv://cannabisAdmin:NQm1eLGJ0YvF7AI3@cannabisculture.c7xlqz7.mongodb.net/cannabisculture?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client["cannabisculture"]
emails_collection = db["emails"]

print("Conexão OK!")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>pekoepa</h1> mis panas")

# import pymongo
# from django.conf import settings
# my_client = pymongo.MongoClient(settings.DB_NAME)

# dbname = my_client['osuVote']

# collection_name = dbname['player']

# p1 = {
#     "userid": 1234,
#     "name": "calpi",
# }

# p2 = {
#     "userid": 4321,
#     "name": "gonzalo",
# }

# collection_name.insert_many([p1, p2])

# players = collection_name.find({})

# for p in players:
#     print(r["name"])

# update_data = collection_name.update_one({'userid': 3333}, {'$set':{'name':'calpi'}})

# count = collection_name.count()
# print(count)

# delete_data = collection_name.delete_one({"userid":4321})
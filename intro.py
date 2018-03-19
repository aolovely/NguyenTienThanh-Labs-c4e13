from pymongo import MongoClient
mongo_uri = "mongodb://khue:khue@ds117489.mlab.com:17489/c4e16-lab"
#connect database
client = MongoClient(mongo_uri)
# get database
db = client.get_default_database()
# create collection
games = db["games"]
blogs = db["nlogs"]
#create a new document
new_game = {
    "name" : "ban ga",
    "description" : "langue of legend"

}

# insert document into collection
games.insert_one(new_game)


all_game = games.find()
for game in all_game:
    print(game)

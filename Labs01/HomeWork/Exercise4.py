from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

db = client.get_default_database()
customers = db["customers"]
events = 0
wom = 0
ads = 0

for customer in customers.find():
    if customer["ref"] == "events":
        events += 1
    elif customer["ref"] == "wom":
        wom += 1
    else:
        ads += 1
print("Number of customers group by refs: events : {0}, wom : {1}, ads : {2}".format(events, wom, ads))

labels1 = ["events", "wom", "ads"]
values1 = [events, wom, ads]
colors1 = ["red", "green", "gold"]
pyplot.pie(values1, labels=labels1, colors= colors1, shadow = True)
pyplot.axis('equal')
pyplot.show()

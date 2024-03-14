import firebase_admin
from firebase_admin import db, credentials
from entity_extractor import *

cred = credentials.Certificate("credentials.json")
print(firebase_admin.initialize_app(cred, {"databaseURL": "https://accivision-2681e-default-rtdb.asia-southeast1.firebasedatabase.app/"}))

ref = db.reference("/")

ref.get()

ref.get()
road_ref = db.reference("/roads")

accident_data = db.reference("/accidents").get()
# road_ref.child("sample").set({"road_class":5,"road_length":1.56,"number_of_accidents":30,"accidents_with_injuries":10,"average_time_clear":9})
# roads = []
large_roads = ['c5','c3','edsa','commonwealth']
accident_locations = []
for data in accident_data.values():
    accident_locations.append(data["location"])
    afterClean = data["location"].replace(",","")
    tokens = afterClean.split(" ")
    # if "aguinaldo" in tokens:
    #     print(tokens)
    if tokens[0] in large_roads:
        road = tokens[0]
    else:
        road = tokens[0] + " " + tokens[1]
    road_data = db.reference("/roads").get()
    if road not in road_data.keys():
        road_ref.child(road.replace("."," ")).set({"road_class":5,"road_length":1.56,"number_of_accidents":30,"accidents_with_injuries":10,"average_time_clear":9})


# This is for inserting data into the accident database
# data = extractor()

# for i in data:
#     db.reference("/accidents").push().set(i)





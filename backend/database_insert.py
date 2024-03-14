import firebase_admin
from firebase_admin import db, credentials
from entity_extractor import *

cred = credentials.Certificate("credentials.json")
print(firebase_admin.initialize_app(cred, {"databaseURL": "https://accivision-2681e-default-rtdb.asia-southeast1.firebasedatabase.app/"}))

ref = db.reference("/")

ref.get()

ref.get()


def insert_roads(accident_data):
    road_ref = db.reference("/roads")
    # roads = []
    accident_locations = []
    for data in accident_data:
        accident_locations.append(data["location"])
        afterClean = data["location"].replace(",","")
        tokens = afterClean.split(" ")
        # if "aguinaldo" in tokens:
        #     print(tokens)
        road = (tokens[0] + " " + tokens[1]).replace("."," ")
        road_data = db.reference("/roads").get()
        if road not in road_data.keys():
            injury_present = 1 if data["presence_of_injuries"] == True else 0
            road_ref.child(road).set({"road_class":5,"road_length":1.56,"number_of_accidents":1,"accidents_with_injuries":injury_present,"average_time_clear":9})
        else:
            existing_road_data = db.reference(f'/roads/{road}').get()
            road_ref.child(road).update({"number_of_accidents":(existing_road_data["number_of_accidents"]+1)})
            if data["presence_of_injuries"] == True:
                road_ref.child(road).update({"accidents_with_injuries":(existing_road_data["accidents_with_injuries"]+1)})
                


# This is for inserting data into the accident database
def add_accidents():
    accident_data = extractor()
    insert_roads(accident_data)
    # for i in data:
    #     db.reference("/accidents").push().set(i)
        
def count_accidents(accidents,road):
    pass


road_ref = db.reference("/roads")
# road_ref.child("sample").set({"road_class":5,"road_length":1.56,"number_of_accidents":30,"accidents_with_injuries":10,"average_time_clear":9})     # This is used when adding a sample value to the roads database
accident_data = db.reference("/accidents").get()
insert_roads(accident_data.values())








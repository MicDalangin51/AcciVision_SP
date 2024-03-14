import re
from datetime import datetime

def convert_to_military(str1): 
     
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
             
    elif str1[-2:] == "AM": 
        return str1[:-2] 
     
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
         
    else: 
         
        # add 12 to hours and remove PM 
        if len(str1) > 6:
            if (int(str1[:2])>12): 
                return str1[:5]
            else:
                return str(int(str1[:2]) + 12) + str1[2:5] 
        else: 
            return str(int(str1[0]) + 12) + str1[1:4] 

def extract_entities(text):
    text = text.lower()
    x = re.search(r"[^\(]+\(",text)
    x_preprocess = x.group()
    location = x_preprocess[:-2]


    y = re.search(r"\(.*\)",text)
    splitted = y.group().split("; ")
    vehicles = splitted[0][1:len(splitted[0])]
    crash_type = splitted[1]
    if re.search(r"injured",text):
        injury = True
    else:
        injury = False
    time = str(convert_to_military(re.search(r"[0123456789]{1,2}:[0123456789]{2}(am|pm)",splitted[2]).group().upper()))
    if len(splitted) > 5:
        if re.search(r"[0123456789]{1,2}:[0123456789]{2}(am|pm)",splitted[5]):
            # print("Time cleared is ",datetime.strptime(convert_to_military(re.search(r"[0123456789]{1,2}:[0123456789]{2}(am|pm)",splitted[5]).group().upper()), "%H:%M"))
            time_to_clear = str(datetime.strptime(convert_to_military(re.search(r"[0123456789]{1,2}:[0123456789]{2}(am|pm)",splitted[5]).group().upper()), "%H:%M") - datetime.strptime(time, "%H:%M"))
        else:
            time_to_clear = str(datetime.strptime(time, "%H:%M") - datetime.strptime(time, "%H:%M"))
    else:
        if re.search(r"cleared upon report",text):
            time_to_clear = str(datetime.strptime(time, "%H:%M") - datetime.strptime(time, "%H:%M"))
        else:
            time_to_clear = "NA"
    entities = {"location":location,"vehicles_involved:":vehicles,"crash_type":crash_type,"time_of_accident":time,"time_to_clear":time_to_clear,"presence_of_injuries":injury}
    return entities

def extractor():
    file = open("testfile.txt", "r")
    date = ''
    accident_entities = []
    for line in file:
        y = re.search(r"^[0-9]{1,2}\.\s",line)
        x = re.search(r"WHEN",line)
        if x:
            date = re.sub(r"(WHEN):\s", "", line)
        if y:
            print(line)
            print("\n")
            new_text = re.sub(r"^[0-9]{1,2}\.\s", "", line)
            e = extract_entities(new_text)
            e['date_occurred'] = date
            accident_entities.append(e)
            
    return accident_entities




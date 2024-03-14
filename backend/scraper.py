from facebook_scraper import get_posts 
from datetime import datetime
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


# Username : Marionne Luna (tipurplehearts1234@gmail.com) Password: pangetka01
# Username: Sean Brown (martin_ivan_dalangin@dlsl.edu.ph)      Password: #SCR@p3R_5T0ol30916^*w
# Username: Leo Hampton (vamptonleo@gmail.com)      Password: #SCR@p3R_5T0ol30916^*w2013

f = open("accident_data.txt", "a")
for post in get_posts("MMDAPH", base_url="https://mbasic.facebook.com", start_url="https://mbasic.facebook.com/MMDAPH?v=timeline", pages=1, credentials=('lebasemarionne@gmail.com','#SCR@p3R_5T0ol30916^*w25')):
    f.write("-----------------------NEW POST------------------------------")
    f.write("\n")
    f.write("Retrieved on: " + str(datetime.now()) + "\n")
    if (post['post_id']):
        f.write("Post ID: " + post['post_id'] + "\n")
    else:
        f.write("Post ID: NO POST ID\n")
    f.write("Posted on: " + str(post['time']) + "\n\n")
    try:
        f.write(post['full_text'])
    except:
        f.write(post['text'])
    f.write("\n")
    f.write("-----------------------END POST---------------------------------\n\n\n")
f.close()
  

  

  

  




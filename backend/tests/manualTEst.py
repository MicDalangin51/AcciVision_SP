import json

from facebook_scraper import get_posts

post = next(get_posts(account=100089065833006, start_url="https://mbasic.facebook.com/<pageId>?v=timeline", cookies='../cks.txt'))
print(post['images'])

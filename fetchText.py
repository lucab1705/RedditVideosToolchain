import praw
import json
import uuid
from secret import CLIENT_ID, CLIENT_SECRET

def load_save_post(url):
    text = reddit.submission(url = url)
    if text.is_self:
        with open(f'./in/unpol_text/{str(uuid.uuid1())}.txt', 'w', encoding="utf-8") as post:
            post.write(text.title+'\n')
            post.write(text.selftext)
            post.close()
    return

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
)

with open('pinnedPosts.json', 'rb') as p:
    posts = json.load(p)
    p.close()

for key in posts['priority']:
    while len(posts['priority'][key]) > 0 :
        url = posts['priority'][key].pop(0)
        load_save_post(url)
    with open('pinnedPosts.json', 'w', encoding="utf-8") as w:
        json.dump(posts, w)
        w.close()

print('No more posts no fetch.')
    
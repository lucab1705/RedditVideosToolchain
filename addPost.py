import sys
import json

PRIORITY = 5

if len(sys.argv) < 2:
    print("Usage: python addPost.py [post link] {priotity (default=5)}")
    exit()

if len(sys.argv) >= 3:
    PRIORITY = sys.argv[2]

pl = open("pinnedPosts.json", "rb")
postList = json.load(pl)
pl.close()
postList['priority'][str(PRIORITY)].append(sys.argv[1])
with open('pinnedPosts.json', 'w') as out:
    json.dump(postList, out)
print('Done.')

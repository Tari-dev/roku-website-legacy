import os
import json

f = open('links.json', 'w')
    
em = {}

for filename in os.listdir('./'):
    if filename.endswith('.py') or filename.endswith('.json'):
       pass
    else:
        img = os.listdir(f'./{filename}/')
        em[filename] = img

json.dump(em ,f, indent=4)
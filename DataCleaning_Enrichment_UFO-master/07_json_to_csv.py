import pandas as pd
import json

data = {}

with open('data/objects.json', 'r') as objects_json:
    objects = json.load(objects_json)['root']

with open('data/captions.json', 'r') as captions_json:
    captions = json.load(captions_json)['root']    


data['sighting_id'] = []
data['objects'] = []
data['caption'] = []
for key, value in objects.items():
    data['sighting_id'].append(key[:5])
    data['objects'].append(', '.join(objects[key]['classnames'][:3]))
    data['caption'].append(captions[key]['captions'][0]['sentence'])


df = pd.DataFrame.from_dict(data)
df.to_csv("part2_data.csv")
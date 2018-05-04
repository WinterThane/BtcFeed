import urllib.request, json
import pandas as pd
from pandas.io.json import json_normalize

jsonurl = urllib.request.urlopen("https://api.cryptowat.ch/assets/btc")
data = json.loads(jsonurl.read())

df = pd.DataFrame(data=data['result']['markets']['base'])
df = df[df['active'] == True]
df = df.sort_values(by=['pair', 'exchange'])

for row in df['pair'] + " - " + df['exchange'] + " - " + df['route']:
    print(row)

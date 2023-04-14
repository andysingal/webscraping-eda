import requests,json,time
import pandas as pd
from pprint import pprint

base_url = "https://official-joke-api.appspot.com/jokes/ten"
r = requests.get(base_url)
print(r.status_code)
# print(len(r.text))
info = r.json()
# print(json.dumps(info, indent=4))

df = pd.DataFrame(info, columns = ['setup', 'punchline'])
pprint(df)

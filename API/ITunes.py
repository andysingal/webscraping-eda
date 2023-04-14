import requests,json
import pandas as pd
from pprint import pprint

base_url = "http://itunes.apple.com/search"

# url = base_url + "?term=beatles&country=us"
# response = requests.get(url)
# print(response.status_code)
r = requests.get(base_url, params={"term":"beatles", "country": "us","limit": 200})
print(r.status_code)
info = r.json()

print(json.dumps(info["results"][0]["releaseDate"], indent=4))

# for result in info['results']:
#     print(result['releaseDate'])
df = pd.DataFrame(info["results"])
pprint(df)
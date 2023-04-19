import requests, json
import pandas as pd

APP_ID =  "846c87a9"
APP_KEY = "367dbef8233306b30fd7791e3f7daa73"

api_endpoint = "https://api.edamam.com/api/nutrition-details"

url = api_endpoint + "?app_id=" + APP_ID + "&app_key=" + APP_KEY

headers = {
    'Content-Type' : 'application/json'
}

recipe = {
    'title' : 'Cappuccino',
    'ingr': ['18g ground expresso', '150ml milk']
}

r = requests.post(url, headers=headers, json=recipe)
print(r.status_code)

capp_info = r.json()
# print(json.dumps(capp_info, indent=4))


# The vertical orientation seems more easier to read
# We achieve that by rotating the dataframe with .transpose()
capp_nutrients = pd.DataFrame(capp_info["totalNutrients"]).transpose()
print(capp_nutrients)

# Exporting the nutrition values to a CSV file
capp_nutrients.to_csv("Cappuccino_nutrients.csv")
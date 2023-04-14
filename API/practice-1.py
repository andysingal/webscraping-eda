import requests,json

base_url = "https://api.apilayer.com/exchangerates_data/latest"
api_key = "PPHbCCQgNCZWTnkRogNGbPrZLDyrB2eK"

response = requests.get(base_url,params={"apikey": api_key})
# print(response.text)

#JSON
# print(json.dumps(response.json(), indent=4))

#print the key features
print(response.json().keys())

#INCORPORATING ELEMENTS IN THE GET REQUEST
param_url = base_url + "?symbols=USD,GBP"
print(param_url)
response1 = requests.get(param_url,params={"apikey": api_key})
data = response1.json()
# print(data)

param_url1 = base_url + "?symbols=GBP" + "&" + "base=USD"
datd = requests.get(param_url1,params={"apikey": api_key}).json()
# print(datd)

#Reading historical data
historical_url = base_url + "?date=2016-01-26"
print(historical_url)
response2 = requests.get(historical_url ,params={"apikey": api_key})
data3 = response2.json()
print(json.dumps(data3, indent=4, sort_keys=True))

#EXTRACTING DATA FOR A TIME PERIOD
# args = {'start_at': '2017-04-26', 'end_at': '2018-04-26', 'symbols': 'GBP'}
# time_period = base_url + "/history" + "?start_at=2017-04-26&end_at=2018-04-26"
# print(time_period)
# response3 = requests.get(time_period ,params={"apikey": api_key})
# data4 = response3.json()
# # #Sort in chronological order
# print(json.dumps(data4, indent=4, sort_keys=True))


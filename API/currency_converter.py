import requests
base_url = "https://api.apilayer.com/exchangerates_data/latest"
api_key = "PPHbCCQgNCZWTnkRogNGbPrZLDyrB2eK"

response = requests.get(base_url,params={"apikey": api_key})

date = input("Please enter the date (in the format 'yyyy-mm-dd' or 'latest'): ")
base = input("Convert from (currency): ")
curr = input("Convert to (currency): ")
quan = float(input("How much {} do you want to convert: ".format(base)))
#
# ##***https://xyneth.netlify.app/work/currency-exchange-rate-api/
url = base_url +  "?date=" + date + "?base=" + base + "&symbols=" + curr
response = requests.get(url, params={"apikey": api_key})

if (response.ok is False):
    print("\nError {}:".format(response.status_code))
    print(response.json())

else:
    data = response.json()
    rate = data['rates'][curr]

    result = quan * rate
#
    print("\n{0} {1} is equal to {2} {3}, based upon exchange rates on {4}".format(quan, base, result, curr,
                                                                                   data['date']))
import requests

time = input("Enter Date: ")
asset_id_base = "BTC"
asset_id_quote = "USD"

url = f"https://rest.coinapi.io/v1/exchangerate/{asset_id_base}/{asset_id_quote}?time={time}"
headers = {'X-CoinAPI-Key': '****'}
response = requests.get(url, headers=headers)

print(response.json())

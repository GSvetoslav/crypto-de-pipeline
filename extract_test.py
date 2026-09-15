import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

try:
    response = requests.get(url, params=params, timeout=10)

    if (response.status_code == 200):
        data = response.json()
        list_variable = data[:3]

        for coin in list_variable:
            print(coin["id"], coin["current_price"])
    else:
        print("Error")
        
    

except requests.exceptions.RequestException as e:
    print(f"Грешка при заявката: {e}")
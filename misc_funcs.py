import http.client
import requests
import json

from nsetools import Nse
from clint.textui import colored

import settings

# Weather
def get_weather():

    location = settings.WEATHER_LOCATION
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={settings.WEATHER_API_KEY}&units=metric"

    site = requests.get(BASE_URL)

    if site.status_code == 200:
        json_data = json.loads(site.text)

        print("Today's weather in", location)
        print("------------------------------")
        print(f"Temperature: {json_data['main']['temp']}°C")
        print(f"Humidity: {json_data['main']['humidity']}")
        print(f"Max Temperature: {json_data['main']['temp_max']}°C")
        print(f"Min Temperature: {json_data['main']['temp_min']}°C")
        print(f"Description: {json_data['weather'][0]['description']}")
        print()
    else:
        print("Invalid API Key\n")


# Football
def get_pl_table():

    connection = http.client.HTTPConnection('api.football-data.org')

    headers = { 'X-Auth-Token': settings.FOOTBALL_API_TOKEN}
    connection.request('GET', '/v2/competitions/2021/standings', None, headers )

    response = json.loads(connection.getresponse().read().decode())

    if response.get('errorCode') == 400:
        print("Invalid API Token.")
    else:
        table_data = response['standings'][0]['table']

        print("\n\n{:<4}| {:<28} | {:<2} | {:<2} | {:<2} | {:<2} | {:<2}".format("Pos", "Team", "GP", "W", "D", "L", "Pts"))
        print("-------------------------------------------------------------")
        for i in table_data:
            print("{:<4}| {:<28} | {:<2} | {:<2} | {:<2} | {:<2} | {:<2}".format(i['position'], i['team']['name'], i['playedGames'],
                                                                                i['won'], i['draw'], i['lost'], i['points']))

        print("\nFootball data provided by the Football-Data.org API")



# Stock Market
def print_stock_data(data):
    print_string = "{:<10} | {:<9} | {:<7} | {:<7} | {:<7} | {:<7} | {:<7} | {:<6} | {:<10} | {:<10} | {:<2}".format(data['Symbol'], data['Average Price'], data['LTP'],
                                                             data['Open'], data['High'], data['Low'], data['Close'],
                                                             data['Change'], data['Previous Close'], data['Qty Traded'],
                                                             data['Market Type'])
    if data['color_status'] == 1:
        print(colored.red(print_string))
    else:
        print(colored.green(print_string))


def extract_stock_data(stock_data):
    return {
        "Symbol": stock_data.get('symbol', "Null"),
        "Average Price": stock_data.get("averagePrice", "Null"),
        "LTP": stock_data.get("lastPrice", "Null"),
        "Open": stock_data.get("open", "Null"),
        "High": stock_data.get("dayHigh", "Null"),
        "Low": stock_data.get("dayLow", "Null"),
        "Close": stock_data.get("close", "Null"),
        "Change": stock_data.get("change", "Null"),
        "Previous Close": stock_data.get("previousClose", "Null"),
        "Qty Traded": stock_data.get("quantityTraded", "Null"),
        "Market Type": stock_data.get("marketType", "Null"),
        "color_status": 1 if '-' in str(stock_data.get("change")) else 0,
    }


def get_stock_details():
    nse = Nse()
    print("{:<10} | {:<7} | {:<7} | {:<7} | {:<7} | {:<7} | {:<7} | {:<6} | {:<7} | {:<10} | {:<2}".format(
        "Symbol", "Avg Price", "LTP", "Open", "High", "Low", "Close", "Change", "Prev Close", "Qty Traded",
        "Market Type"
    ))
    for stock in settings.STOCKS:
        stock_data = nse.get_quote(stock)
        stock_data = extract_stock_data(stock_data)
        print_stock_data(stock_data)




if __name__ == "__main__":
    get_stock_details()

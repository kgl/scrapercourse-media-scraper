import requests
import os


stocks = ['2330', '006208']

for stock in stocks:
    response = requests.get(
        f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=20221104&stockNo={stock}')

    if not os.path.exists('csv'):
        os.makedirs('csv')

    with open(f'csv/{stock}.csv', 'wb') as file:
        file.write(response.content)

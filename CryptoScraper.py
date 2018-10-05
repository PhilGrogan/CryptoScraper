#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:23:46 2018

@author: phil
"""
from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests as req
import datetime as dt
import csv

now = '{0:%Y-%m-%d_%H%M}'.format(dt.datetime.now())
coins = ['date/time', 'bitcoin', 'ethereum','litecoin', 'ripple']
prices = []
outfile = Path(str(Path.home()) + '/Documents/CoinPrices.csv')


if outfile.exists():
    print(f"do not open file {outfile} while this program is running")
else:
    with open(str(outfile), 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(coins)
        print(f"created file {outfile}; do not open while this program is running")


for name in coins:
    if name == 'date/time':
        prices.append(now)
    else:
        print("retrieving price of", name)
        page = req.get('https://www.worldcoinindex.com/coin/' + name)
        soup = bs(page.text, 'html.parser')
        price_box = soup.find('div', attrs={'class':'coinprice'})
        price = price_box.text.strip().replace("\n", '').replace("\r", '').replace("$", '').replace(',', '')
        prices.append(float(price))
    
with open(str(outfile), 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(prices)
print(f"all data written to file {outfile}; file is safe to open")
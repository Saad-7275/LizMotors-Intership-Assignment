#!/usr/bin/env python
# coding: utf-8

# In[21]:


import requests
from bs4 import BeautifulSoup
import csv

def fetch_data(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    response = requests.get(url)
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        company_name = soup.find('h1',class_ ='D(ib)').text
        current_price = soup.find('div', class_= 'My(6px) Pos(r) smartphone_Mt(6px)')
        if company_name and current_price:
            company_name = company_name.text.strip()
            current_price = current_price.text.strip()
        previous_close = soup.find('span', text='Previous Close').find_next('td')
        open_price = soup.find('span', text='Open').find_next('td')
        if previous_close and open_price:
            previous_close = previous_close.text.strip()
            open_price = open_price.text.strip()
        
        data = {
            'Company Name': company_name,
            'Current Price': current_price,
            'Previous Close': previous_close,
            'Open Price': open_price
        }
        return data
    else:
        print("Failed to fetch data")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

def main():
    ticker = "GOEV"
    data = fetch_data(ticker)
    if data:
        filename = f"{ticker}_data.csv"
        save_to_csv(data, filename)
        print(f"Data saved to {filename}")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    main()


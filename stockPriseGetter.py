import requests
from bs4 import BeautifulSoup
from datetime import datetime

class stockGetPrice:
    stocks_dict = {
        "Apple": "AAPL",
        "Microsoft Corp": "MSFT",
        "Tesla Inc": "TSLA"
    }

    @staticmethod
    def getStockPrice(index):
        url = f'https://www.google.com/finance/quote/{index}:NASDAQ'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_price_class = "YMlKec fxKbKc"
        price = float(soup.find(class_=div_price_class).text.strip()[1:].replace(",", ""))
        return price

    def getPrice(self):
        prices = {}
        for name, value in self.stocks_dict.items():
            price = self.getStockPrice(value)
            prices[name] = price
        
        # Convert datetime object to string
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        prices['date'] = current_time
        return prices
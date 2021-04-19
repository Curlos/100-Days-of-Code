from price import PriceTracker
from stock import StockTracker

"""def scrape_stock():
    notify_by = int(input("How would you like to be notified when the item is back in stock?"
                          "Enter a number from 1-3 from the following options: "
                          "\n1. Text"
                          "\n2. Email"
                          "\n3. Both Text and Email\n"))

    product_html, URL = scrape_page()
    soup = BeautifulSoup(product_html, "html.parser")
    in_stock = soup.select_one("#availability").getText().replace('\n', '').strip()

    if 'in stock' in in_stock.lower():

        print('YAHOO!')
    print(in_stock)"""


stock_tracker = StockTracker()
stock_tracker.check_in_stock()


import argparse 
import requests
from bs4 import BeautifulSoup
import json
import re


# bronzer, squishmallow, electric guitar

# get command line arguments
parser = argparse.ArgumentParser(description='Download Information from Ebay and Convert to JSON')
parser.add_argument('search_term')
args = parser.parse_args()
print('args.search_term=', args.search_term)

# list of all items found in ebay
items = []

for page_number in range(1, 11):

    # build the url
    url = 'https://www.ebay.com/sch/i.html?_nkw=' 
    url += args.search_term  
    url += '&_sacat=0&_pgn='
    url += str(page_number)
    print('url=', url)

    # download the html
    r = requests.get(url)
    status = r.status_code
    print('status=', status)

    html = r.text

    # process the html
    soup = BeautifulSoup(html, 'html.parser')

    tags_items = soup.select('.s-item')
    for tag_items in tags_items:

        tags_name = tag_items.select('.s-item__title')
        name = None
        for tag in tags_name:
            name = tag.text
        if name is None or name.strip() == "Shop on eBay":
            continue

        tags_freereturns = tag_items.select('.s-item__free-returns')
        freereturns = False
        for tag in tags_freereturns:
            freereturns = True

        items_sold = None
        tags_itemssold = tag_items.select('.s-item__quantitySold')
        for tag in tags_itemssold:
            items_sold = tag.text

        item_status = None
        tags_itemstatus = tag_items.select('.SECONDARY_INFO')
        for tag in tags_itemstatus:
            item_status = tag.text

        shipping_price = None
        tags_shippingprice = tag_items.select('.s-item__shipping')
        for tag in tags_shippingprice:
            shipping_text = tag.text.strip()
            if 'free' in shipping_text.lower():
                shipping_price = 0
            else:
                match = re.search(r'\$([\d,.]+)', shipping_text)
                if match:
                    shipping_price = int(float(match.group(1).replace(',', '')) * 100)
        
        item_price = None
        tags_itemprice = tag_items.select('.s-item__price')
        for tag in tags_itemprice:
            match = re.search(r'\$([\d,.]+)', tag.text)
            if match:
                item_price = int(float(match.group(1).replace(',', '')) * 100)

        item = {
            'name': name,
            'freereturns': freereturns,
            'items_sold': items_sold,
            'item_status': item_status,
            'shipping_price': shipping_price,
            'item_price': item_price
        }
        items.append(item)
            
    print('len(tags_items)=', len(tags_items))

    for item in items:
        print('item=', item)


filename = args.search_term+'.json'
with open(filename, 'w', encoding='ascii') as f:
    f.write(json.dumps(items ))

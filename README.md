# Project 3: eBay Scrapping

## What the Python File Does

The `ebay-dl.py` file is a Python web scraper that uses requests, argparse, and BeautifulSoup to exract data from product listings in an eBay search. For each item, it collects the title of the listing, whether it has free returns, the amount sold, the condition of the item, shipping cost in cents, and the price of the item in cents. After this data is collected, the Python file then puts all this information into a `JSON` file. 

## How to run the Python File
To run the script and generate the `.json` output, use the command line. The script uses argparse to accept the search term as an argument. For example, if we wanted to find data for squishmallows, we input `python3 ebay-dl.py squishmallows` into our terminal. If its a multispaced search term, then the input is `python3 ebay-dl.py 'electric guitar'`.

## Link to Course Project
[Press Here](https://github.com/mikeizbicki/cmc-csci040/tree/2025spring/project_03_webscraping)


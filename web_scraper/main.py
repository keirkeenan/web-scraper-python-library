# disable the following pylint warnings:
# pylint: disable=missing-module-docstring,
# pylint: disable=pointless-string-statement,
# pylint: disable=missing-function-docstring
# pylint: disable=no-else-return
# pylint: disable=line-too-long

import json
import datetime
import random
import time
import requests
from bs4 import BeautifulSoup


"""This function gets the html from the website"""


def get_html(company_name, product_name, page_number):
    if company_name == "ebay":
        # build the url
        url_product = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={product_name}"
        url_page = f"&_sacat=0&_pgn={page_number}"
        url = url_product + url_page

        # download the html
        req = requests.get(url, timeout=5)
        html = req.text

        return html

    elif company_name == "walmart":
        # build the url
        url_product = f"https://www.walmart.com/search?q={product_name}"
        url_page = f"&page={page_number}&affinityOverride=default"
        url = url_product + url_page
        ac1 = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
        ac2 = "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        acc = ac1 + ac2
        user_agent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        user_agent2 = "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        user_agent = user_agent1 + user_agent2
        headers = {
            "Referer": "https://www.google.com",
            "Connection": "Keep-Alive",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": acc,
            "User-Agent": user_agent,
        }

        # download the html
        req = requests.get(url, headers=headers, timeout=5)
        html = req.text

        return html

    elif company_name == "amazon":
        # build the url
        url = f"https://www.amazon.com/s?k={product_name}&page={page_number}"
        ac1 = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
        ac2 = "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        acc = ac1 + ac2
        user_agent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        user_agent2 = "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        user_agent = user_agent1 + user_agent2
        headers = {
            "Referer": "https://www.google.com",
            "Connection": "Keep-Alive",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": acc,
            "User-Agent": user_agent,
        }

        # download the html
        req = requests.get(url, headers=headers, timeout=5)
        html = req.text

        return html

    else:
        return "Something went wrong. Please try again."


"""This is the parse_itemprice function that will parse the price of the item"""


def parse_itemprice(text):
    start = 0
    end = 0
    price_str = ""
    text = text.replace(",", "")
    start = text.find("$")
    end = text.find(".")
    price_str = text[start + 1 : end]
    price_str += text[end : end + 3]
    price = float(price_str)
    return price


"""eBay web scraper"""


def scrape_ebay(product_name):
    print("Scraping eBay...")

    items = []

    # loop over the eBay webpages (3 pages)
    for page_number in range(1, 4):
        # random sleep
        time.sleep(random.randint(1, 6))

        # get the html & process it
        soup = BeautifulSoup(get_html("ebay", product_name, page_number), "html.parser")

        # loop over the items in the page
        tags_items = soup.select(".s-item")
        for tag_item in tags_items:
            name = None
            for tag in tag_item.select(".s-item__title"):
                name = tag.text

            price = None
            for tag in tag_item.select(".s-item__price"):
                price = parse_itemprice(tag.text)

            status = None
            for tag in tag_item.select(".s-item__subtitle"):
                status = tag.text

            if name is not None and price is not None:
                item = {
                    "company": "eBay",
                    "name": name,
                    "price": price,
                    "status": status,
                    "extraction_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
                items.append(item)

    # write json to stdout
    data = json.dumps(items, indent=2)

    # Check if the file is not empty
    if len(data) > 2:
        print("eBay Scraper Success!")
        time.sleep(2)
        return data
    else:
        return "Failed to collect data from eBay. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"


"""Walmart web scraper"""


def scrape_walmart(product_name):
    print("Scraping Walmart...")

    items = []

    # loop over the Walmart webpages (3 pages)
    for page_number in range(1, 4):
        # random sleep
        random_sleep = random.randint(1, 6)
        time.sleep(random_sleep)

        # get the html
        html = get_html("walmart", product_name, page_number)

        # process the html
        soup = BeautifulSoup(html, "html.parser")

        # loop over the items in the page
        products = soup.find_all("div", class_="sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity")

        for product in products:
            try:
                name = product.find("span", class_="w_V_DM").text
            except AttributeError:
                name = None
            try:
                price = product.find("div", class_="mr1 mr2-xl b black green lh-copy f5 f4-l").text
                price = parse_itemprice(price)
            except AttributeError:
                price = None

            if name is not None and price is not None:
                item = {
                    "company": "Walmart",
                    "name": name,
                    "price": price,
                    "extraction_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
                items.append(item)

    # write json to stdout
    data = json.dumps(items, indent=2)

    # Check if the file is not empty
    if len(data) > 2:
        print("Walmart Scraper Success!")
        time.sleep(2)
        return data
    else:
        return "Failed to collect data from Walmart. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"


"""Amazon web scraper"""


def scrape_amazon(product_name):
    print("Scraping Amazon...")

    items = []

    # loop over the Amazon webpages (3 pages)
    for page_number in range(1, 4):
        # random sleep
        random_sleep = random.randint(1, 6)
        time.sleep(random_sleep)

        # get the html
        html = get_html("amazon", product_name, page_number)

        # process the html
        soup = BeautifulSoup(html, "html.parser")

        # loop over the items in the page
        products = soup.find_all(
            "div",
            class_="a-section a-spacing-small puis-padding-left-small puis-padding-right-small",
        )

        for product in products:
            try:
                name = product.find("span", class_="a-size-base-plus a-color-base a-text-normal").text
            except AttributeError:
                name = None
            try:
                price = product.find("span", class_="a-offscreen").text
                price = parse_itemprice(price)
            except AttributeError:
                price = None

            if name is not None and price is not None:
                item = {
                    "company": "Amazon",
                    "name": name,
                    "price": price,
                    "extraction_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
                items.append(item)

    # write json to stdout
    data = json.dumps(items, indent=2)

    # Check if the file is not empty
    if len(data) > 2:
        print("Amazon Scraper Success!")
        time.sleep(2)
        return data
    else:
        return "Failed to collect data from Amazon. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"


"""Main function that takes in the product name and company name"""


def scrape(product_name, company_name):
    # scrape the websites
    if company_name.lower() == "ebay":
        return scrape_ebay(product_name)
    elif company_name.lower() == "walmart":
        return scrape_walmart(product_name)
    elif company_name.lower() == "amazon":
        return scrape_amazon(product_name)
    else:
        return f"Scraper not available for `{company_name}`. Try: eBay, Walmart, or Amazon."

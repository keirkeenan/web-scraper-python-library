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


def get_html(company_name, product_name, page_number):
    '''
    This function gets the html from the website.

    :param company_name: The name of the company to be scraped
    :type company_name: str
    :param product_name: The name of the product to be scraped
    :type product_name: str
    :param page_number: The page number of the website to be scraped
    :type page_number: int
    :return: The html of the website
    :rtype: str

    '''
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
        ac1 = "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8"
        ac2 = "gzip, deflate, br"
        acc = ac1 + ac2
        user_agent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        user_agent2 = "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        user_agent = user_agent1 + user_agent2
        headers = {
            "Referer": "https://www.google.com",
            "Connection": "keep-alive",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": acc,
            "Accept": ac1,
            "User-Agent": user_agent,
        }

        # download the html
        req = requests.get(url, headers=headers, timeout=5)
        html = req.text

        return html

    else:
        return "Something went wrong. Please try again."


def parse_itemprice(text):
    '''
    This function parses the price of the item.

    :param text: The text to be parsed
    :type text: str
    :return: The price of the item
    :rtype: float

    '''
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


def parse_rating(text):
    '''
    This function parses the rating of the item.

    :param text: The text to be parsed
    :type text: str
    :return: The rating of the item
    :rtype: float

    '''

    end = 0
    rating_str = ""
    end = text.find(" out")
    rating_str = text[:end]
    rating = float(rating_str)
    return rating


"""eBay web scraper"""


def scrape_ebay(product_name):
    '''
    This function scrapes the eBay website for the product name and returns the data in JSON format.

    :param product_name: The name of the product to be scraped
    :type product_name: str
    :return: The data in JSON format
    :rtype: str

    '''
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
    '''
    This function scrapes the Walmart website for the product name and returns the data in JSON format.

    :param product_name: The name of the product to be scraped
    :type product_name: str
    :return: The data in JSON format
    :rtype: str

    '''
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
    '''
    This function scrapes the Amazon website for the product name and returns the data in JSON format.

    :param product_name: The name of the product to be scraped
    :type product_name: str
    :return: The data in JSON format
    :rtype: str

    '''
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

        # loop over all products with <div data-asin="...">
        products = soup.find_all("div", {"data-asin": True})

        for product in products:
            try:
                asin = product["data-asin"]
            except AttributeError:
                asin = None
            try:
                name = product.find("span", class_="a-size-medium a-color-base a-text-normal").text
            except AttributeError:
                name = None
            try:
                price = product.find("span", class_="a-offscreen").text
                price = parse_itemprice(price)
            except AttributeError:
                price = None
            try:
                rating = product.find("span", class_="a-icon-alt").text
                rating = parse_rating(rating)
            except AttributeError:
                rating = None
            try:
                num_ratings = product.find("span", class_="a-size-base s-underline-text").text
                num_ratings = float(num_ratings.replace(",", "").replace(" ratings", ""))
            except AttributeError:
                num_ratings = None
            try:
                image_url = product.find("img")["src"]
            except (TypeError, AttributeError):
                image_url = None
            try:
                url = (
                    "https://www.amazon.com"
                    + product.find(
                        "a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"
                    )["href"]
                )
            except (TypeError, AttributeError):
                url = None

            if name is not None and price is not None:
                item = {
                    "company": "Amazon",
                    "asin": asin,
                    "name": name,
                    "price": price,
                    "extraction_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "rating": rating,
                    "num_ratings": num_ratings,
                    "image_url": image_url,
                    "url": url,
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
    '''
    This function takes in the product name and company name and returns the data in JSON format.

    :param product_name: The name of the product to be scraped
    :type product_name: str
    :param company_name: The name of the company to be scraped
    :type company_name: str
    :return: The data in JSON format
    :rtype: str

    '''

    # scrape the websites
    if company_name.lower() == "ebay":
        return scrape_ebay(product_name)
    elif company_name.lower() == "walmart":
        return scrape_walmart(product_name)
    elif company_name.lower() == "amazon":
        return scrape_amazon(product_name)
    else:
        return f"Scraper not available for `{company_name}`. Try: eBay, Walmart, or Amazon."


"""Function that takes in the product name and scrapes all available websites"""


def scrape_all(product_name):
    '''
    This function takes in the product name and scrapes all available websites.

    :param product_name: The name of the product to be scraped
    :type product_name: str
    :return: The data in JSON format
    :rtype: str

    '''

    # scrape the websites
    amazon = scrape_amazon(product_name)
    walmart = scrape_walmart(product_name)
    ebay = scrape_ebay(product_name)

    # combine the json strings into a list
    combined_list = []

    if (
        amazon
        != "Failed to collect data from Amazon. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
    ):
        combined_list += json.loads(amazon)
    if (
        walmart
        != "Failed to collect data from Walmart. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
    ):
        combined_list += json.loads(walmart)
    if (
        ebay
        != "Failed to collect data from eBay. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
    ):
        combined_list += json.loads(ebay)

    combined_json_string = json.dumps(combined_list, indent=2)

    # Check if the file is not empty
    if len(combined_json_string) > 2:
        return combined_json_string
    else:
        return "Failed to collect any data. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"

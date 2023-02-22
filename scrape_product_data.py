import requests
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# performs an HTTP request to retrieve the HTML content of a given URL
def get_html(url):
    response = requests.get(url)
    html = response.content
    return html

# spins up a local browser to load a given URL
def open_browser(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver.page_source

# parse a single page of HTML content and extracts relevant product information from Amazon, Walmart, and Best Buy
def parse_amazon(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('span', {'id': 'productTitle'}).text.strip()
    price = soup.find('span', {'class': 'a-price-whole'}).text.strip()
    rating = soup.find('span', {'class': 'a-icon-alt'}).text.strip()
    reviews = soup.find('span', {'id': 'acrCustomerReviewText'}).text.strip()
    product_data = {
        'title': title,
        'price': price,
        'rating': rating,
        'reviews': reviews
    }
    return product_data

def parse_walmart(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1', {'class': 'prod-ProductTitle'}).text.strip()
    price = soup.find('span', {'class': 'price-characteristic'}).text.strip()
    rating = soup.find('span', {'class': 'seo-avg-rating'}).text.strip()
    reviews = soup.find('span', {'class': 'seo-review-count'}).text.strip()
    product_data = {
        'title': title,
        'price': price,
        'rating': rating,
        'reviews': reviews
    }
    return product_data

def parse_bestbuy(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1', {'class': 'heading-5 v-fw-regular'}).text.strip()
    price = soup.find('div', {'class': 'priceView-hero-price priceView-customer-price'}).text.strip()
    rating = soup.find('div', {'class': 'ugc-c-review-average'}).text.strip()
    reviews = soup.find('span', {'class': 'c-review-average'}).text.strip()
    product_data = {
        'title': title,
        'price': price,
        'rating': rating,
        'reviews': reviews
    }
    return product_data

# combines the previous helper functions to scrape a single page of product data and returns the data as a pandas dataframe
def scrape_product(sku, url):
    html = get_html(url)
    product_data = parse_html(html)
    df = pd.DataFrame(product_data)
    return df

# scrapes multiple products given a list of product information and a URL template. The URL template should contain placeholders for the product information (e.g. {sku} or {product_name}) that can be replaced with the actual values
def scrape_multiple_products(product_list, url_template):
    dfs = []
    for product in product_list:
        url = url_template.format(**product)
        df = scrape_product(product['sku'], url)
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

# compares the price across Amazon, Walmart, and Best Buy
def compare(product_name):
    # define the URLs for the product on each site
    amazon_url = f'https://www.amazon.com/s?k={product_name}'
    walmart_url = f'https://www.walmart.com/search?q={product_name}'
    bestbuy_url = f'https://www.bestbuy.com/site/searchpage.jsp?st={product_name}'
    
    # scrape the product data from each site
    amazon_data = scrape_product(product_name, amazon_url)
    walmart_data = scrape_product(product_name, walmart_url)
    bestbuy_data = scrape_product(product_name, bestbuy_url)
    
    # extract the price data from each site's data
    amazon_price = float(amazon_data.loc[0, 'price'].replace('$', ''))
    walmart_price = float(walmart_data.loc[0, 'price'].replace('$', ''))
    bestbuy_price = float(bestbuy_data.loc[0, 'price'].replace('$', ''))
    
    # print the price data for each site
    print(f"Amazon: ${amazon_price:.2f}")
    print(f"Walmart: ${walmart_price:.2f}")
    print(f"Best Buy: ${bestbuy_price:.2f}")
    
    # determine which site has the lowest price
    lowest_price = min(amazon_price, walmart_price, bestbuy_price)
    if lowest_price == amazon_price:
        print("Amazon has the lowest price.")
    elif lowest_price == walmart_price:
        print("Walmart has the lowest price.")
    else:
        print("Best Buy has the lowest price.")

'''
Example usage:
compare('iPhone 13')
'''



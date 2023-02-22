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

# retrieves customer reviews for a product from a given website
def get_product_reviews(product_name, url):
    # determine the site and call the appropriate function to scrape the review data
    if 'amazon' in url:
        html = get_html(url)
        review_data = parse_amazon_reviews(html)
    elif 'walmart' in url:
        html = get_html(url)
        review_data = parse_walmart_reviews(html)
    elif 'bestbuy' in url:
        html = get_html(url)
        review_data = parse_bestbuy_reviews(html)
    else:
        print(f"Unsupported URL: {url}")
        review_data = {}
    
    # add the site name and product name to the review data and return as a DataFrame
    review_data['site'] = url.split('.')[1]
    review_data['product'] = product_name
    review_df = pd.DataFrame(review_data)
    return review_df

# retrieves a list of related products for a given product from a given website
def get_related_products(product_name, url):
    # determine the site and call the appropriate function to scrape the related product data
    if 'amazon' in url:
        html = get_html(url)
        related_data = parse_amazon_related(html)
    elif 'walmart' in url:
        html = get_html(url)
        related_data = parse_walmart_related(html)
    elif 'bestbuy' in url:
        html = get_html(url)
        related_data = parse_bestbuy_related(html)
    else:
        print(f"Unsupported URL: {url}")
        related_data = {}
    
    # add the site name and product name to the related product data and return as a DataFrame
    related_data['site'] = url.split('.')[1]
    related_data['product'] = product_name
    related_df = pd.DataFrame(related_data)
    return related_df

# retrieves the availability of a product for a given website
def get_product_availability(product_name, url):
    # determine the site and call the appropriate function to scrape the store availability data
    if 'amazon' in url:
        availability_data = {}
    elif 'walmart' in url:
        html = get_html(url)
        availability_data = parse_walmart_availability(html)
    elif 'bestbuy' in url:
        html = get_html(url)
        availability_data = parse_bestbuy_availability(html)
    else:
        print(f"Unsupported URL: {url}")
        availability_data = {}
    
    # add the site name and product name to the store availability data and return as a DataFrame
    availability_data['site'] = url.split('.')[1]
    availability_data['product'] = product_name
    availability_df = pd.DataFrame([availability_data])
    return availability_df


# Tests
def main():
    # test the scrape_product function
    amazon_data = scrape_product('iPhone 13', 'https://www.amazon.com/s?k=iPhone+13')
    print(amazon_data)
    walmart_data = scrape_product('iPhone 13', 'https://www.walmart.com/search?q=iPhone+13')
    print(walmart_data)
    bestbuy_data = scrape_product('iPhone 13', 'https://www.bestbuy.com/site/searchpage.jsp?st=iPhone+13')
    print(bestbuy_data)
    
    # test the compare function
    compare('iPhone 13')
    '''
    This will scrape the product data for the iPhone 13 on Amazon, Walmart, and Best Buy, extract the price data, print the prices for each site, and determine which site has the lowest price. 
    NOTE: This function assumes that the first search result on each site corresponds to the desired product. Since this may not always be the case, we will want to modify the code in future updates.
    '''

    # test usage of `get_product_reviews`
    amazon_reviews = get_product_reviews('iPhone 13', 'https://www.amazon.com/dp/B09G9P3WVR')
    print(amazon_reviews.head())

    # test usage of `get_related_products`
    walmart_related = get_related_products('Apple Watch Series 7', 'https://www.walmart.com/ip/Apple-Watch-Series-7-GPS-41mm-Product-RED-Aluminum-Case-with-PRODUCT-RED-Sport-Band/657943300')
    print(walmart_related.head())

    # test usage of `get_product_availability`
    bestbuy_availability = get_product_availability('Nintendo Switch OLED', 'https://www.bestbuy.com/site/nintendo-switch-oled-model-blue-yellow-red/6471322.p?skuId=6471322')
    print(bestbuy_availability)

if __name__ == '__main__':
    main()



# Web Scraping - Python Library

A Python library that lets you easily scrape data from popular websites using basic product information

[![](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/license/mit-0/)
[![](https://img.shields.io/github/issues/keirkeenan/web-scraper-python-library)](https://github.com/keirkeenan/web-scraper-python-library/issues)
[![Build Status](https://github.com/keirkeenan/web-scraper-python-library/actions/workflows/build.yml/badge.svg)](https://github.com/keirkeenan/web-scraper-python-library/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/keirkeenan/web-scraper-python-library/branch/main/graph/badge.svg)](https://codecov.io/gh/keirkeenan/web-scraper-python-library)

## Overview

For many, collecting product data can be helpful for monitoring price changes or helping decide which e-commerce site to purchase from. However, creating a web scraper from scratch can be cumbersome and time consuming. My goal is to make it easier for people to collect product data, and this Python library aims to simplify the web scraping process. With basic inputs like product information and store url, you can have easy access to rich product information.

## Installation

To install, run the following:

```
pip install web-scraper-python-library
```

## Usage

### Product Search

The following code will retrieve and print the product data for an `iphone 12` from `Amazon` as a JSON object.

`product`: a product name, like you would put into the product search page of a company's website

`company`: 'eBay', 'Walmart', or 'Amazon'

#### Code

```python
from web_scraper_python_library import main as m

product_data = m.main(product = 'iphone 12', company = 'Amazon')
print(product_data)
```

#### Output

```json
[
  {
    "name": "Apple iPhone 12, 64GB, Green - Fully Unlocked (Renewed)",
    "price": 390.0,
    "extraction_date": "2023-03-23 17:38:32"
  },
  ...
  {
    "name": "Apple iPhone 12 Mini, 64GB, Black - Unlocked (Renewed)",
    "price": 312.0,
    "extraction_date": "2023-03-23 17:38:32"
  }
]
```

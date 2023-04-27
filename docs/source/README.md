# Quick Guide

A Python library that lets you easily scrape data from popular websites using basic product information

[![](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/license/mit-0/)
[![](https://img.shields.io/github/issues/keirkeenan/web-scraper-python-library)](https://github.com/keirkeenan/web-scraper-python-library/issues)
[![Build Status](https://github.com/keirkeenan/web-scraper-python-library/actions/workflows/build.yml/badge.svg)](https://github.com/keirkeenan/web-scraper-python-library/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/keirkeenan/web-scraper-python-library/branch/main/graph/badge.svg)](https://codecov.io/gh/keirkeenan/web-scraper-python-library)
[![PyPI](https://img.shields.io/pypi/v/web-scraper-python-library)](https://pypi.org/project/web-scraper-python-library/)

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
from web_scraper import main as m
import json

json_product_data = m.scrape("iphone 12", "Amazon")
product_data = json.loads(json_product_data)
print(product_data)
```

#### Output

```
[
  {
    "company": "Amazon",
    "asin": "B09HWS3VGM",
    "name": "TCL 10 5G UW 128GB Diamond Gray Smartphone (Verizon) (Renewed)",
    "price": 84.0,
    "extraction_date": "2023-04-27 16:59:56",
    "rating": "3.8 out of 5 stars",
    "num_ratings": 106.0,
    "image_url": "https://m.media-amazon.com/images/I/41e-4yZQl9L._AC_UY218_.jpg",
    "url": "https://www.amazon.com/TCL-Diamond-Smartphone-Verizon-Renewed/dp/B09HWS3VGM/ref=sr_1_42?keywords=iphone+12&qid=1682629195&sr=8-42"
  },
  ...
  {
    "company": "Amazon",
    "asin": "B0BS986JRZ",
    "name": "QIMHAI Smartphone Unlocked Cell Phones S22 Ultra 6.1in HD Screen Cheap Phones 2GB/16GB Android 10 Straight Talk Phone 5000mAh 128GB Extension Dual Sim Boost Mobile Phones Telefonos (Gold)",
    "price": 79.99,
    "extraction_date": "2023-04-27 16:59:56",
    "rating": "1.9 out of 5 stars",
    "num_ratings": 6.0,
    "image_url": "https://m.media-amazon.com/images/I/71fa-n5E69L._AC_UY218_.jpg",
    "url": "https://www.amazon.com/QIMHAI-Smartphone-Unlocked-Extension-Telefonos/dp/B0BS986JRZ/ref=sr_1_43?keywords=iphone+12&qid=1682629195&sr=8-43"
  }
]
```

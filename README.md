# Web Scraping - Python Library

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

The following code will retrieve and print the product data for an `pencil` from `Amazon` as a JSON object.

`product`: a product name, like you would put into the product search page of a company's website

`company`: 'eBay', 'Walmart', or 'Amazon'

#### Code

```python
from web_scraper_python_library import main as m

product_data = m.main(product = 'pencil', company = 'Amazon')
print(product_data)
```

#### Output

```json
[
  {
    "company": "Amazon",
    "name": "Staedtler 0.5mm Mechanical Pencil Silver Series (925 25-05)",
    "price": 11.0,
    "extraction_date": "2023-03-23 17:38:32"
  },
  ...
  {
    "company": "Amazon",
    "name": "Pica Dry Bundle (1 x 3030 Pencil + 1 x 4050 Refill) in Blister Packaging",
    "price": 21.0,
    "extraction_date": "2023-03-23 17:38:32"
  }
]
```

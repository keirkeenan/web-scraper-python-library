# Scraping Functions - Examples

Many developers and data scientists, especially in e-commerce, have trouble collecting real-time, reliable product data. This library comes with tools that make it easy to collect this data from high demand websites.

## Use Product & Company Name

The following code will search **Walmart's** wesbite for **hiking shoes**:

```python
from web_scraper import main as m
import json

json_product_data = m.scrape("hiking", "Walmart")
product_data = json.loads(json_product_data)
print(product_data)
```

## Company Specific

### eBay

The following code will search **eBay's** wesbite for **iphone 12**:

```python
from web_scraper import main as m
import json

json_product_data = m.scrape_ebay("iphone 12")
product_data = json.loads(json_product_data)
print(product_data)
```

### Walmart

The following code will search **Walmart's** wesbite for **dog toys**:

```python
from web_scraper import main as m
import json

json_product_data = m.scrape_walmart("dog toys")
product_data = json.loads(json_product_data)
print(product_data)
```

### Amazon

The following code will search **Amazon's** wesbite for **sunglasses**:

```python
from web_scraper import main as m
import json

json_product_data = m.scrape_amazon("sunglasses")
product_data = json.loads(json_product_data)
print(product_data)
```

## All Websites

The following code will search **all supported websites** for **power tools**:

```python
from web_scraper import main as m
import json

json_product_data = m.scrape_all("power tools")
product_data = json.loads(json_product_data)
print(product_data)
```

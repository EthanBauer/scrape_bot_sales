import pandas as pd
# intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
  
# Create DataFrame
df = pd.DataFrame(data)
  
# Print the output.
print(df)

from bs4 import BeautifulSoup
import requests

# page_to_scrape = requests.get("http://quotes.toscrape.com")
# soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# quotes = soup.findAll("span", attrs={"class":"text"})
# authors = soup.findAll("small", attrs={"class": "author"})

# for quote in quotes:
#     print(quote.text)
# for author in authors:
#     print(author.text)


page_to_scrape = requests.get("https://shop.lululemon.com/en-ca/c/sale/_/N-1z0xcmkZ8t5")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
product_names = soup.findAll("h3", attrs={"class": "product-tile__product-name"})
# <h3 class="product-tile__product-name lll-text-body-1"><a class="link lll-font-weight-medium" data-skuid="ca_147031962" data-productid="prod9740008" data-categoryunifiedid="men-shorts" data-lulu-track="pdp-link" data-lulu-attributes="{&quot;type&quot;:&quot;product&quot;,&quot;product&quot;:{&quot;name&quot;:&quot;At%20Ease%20Short%207%22&quot;,&quot;skuID&quot;:&quot;ca_147031962&quot;,&quot;productID&quot;:&quot;prod9740008&quot;,&quot;categoryUnifiedID&quot;:&quot;at-ease-short-md&quot;,&quot;color&quot;:&quot;61885&quot;,&quot;deliveryType&quot;:&quot;ship&quot;},&quot;attributes&quot;:{&quot;component&quot;:&quot;product-list&quot;,&quot;displayType&quot;:&quot;label&quot;,&quot;position&quot;:1},&quot;version&quot;:&quot;2.1&quot;}" href="/en-ca/p/men-shorts/At-Ease-Short-MD/_/prod9740008?color=61885">At Ease Short 7"</a></h3>
names = []
for product_name in product_names:
    print(product_name.text)
    names.append(product_name.text) 

product_prices = soup.findAll("span", attrs={"class": ""})

prices = []
for product_price in product_prices:
    print(product_price.text)
    prices.append(product_price.text)

print(len(product_names))
print(len(product_prices))

print(names)
print(prices)

for p in prices:
    print(p)
    if(p == '\xa0-\xa0'):
        prices.remove(p)

print(prices)


59 - 78

39-69 - 88

79 - 128

39 - 64

39-49 - 68

84-89 - 118

49 - 68

59-69 - 78

84-99 - 68

84-89 - 118

49 - 68

59-69 - 78

84-99 - 128

39-59 - 64-74

69 - 88

49 - 68

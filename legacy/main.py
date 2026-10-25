from bs4 import BeautifulSoup
import requests
import pandas as pd

listing_title = []
listing_price = []
listing_condition = []
listing_shipping = []
listing_auction = []
no_best_offer = []
items_per_page = 60
number_of_pages = 59


def fetch_item_title(listing):
    try:
        item_title = listing.find("div", class_="s-item__title").text
        listing_title.append(item_title)
    except AttributeError:
        listing_title.append("")


def fetch_item_price(listing):
    try:
        price = listing.find("span", class_="s-item__price").text.strip()
        listing_price.append(price)
    except AttributeError:
        listing_price.append("")


def fetch_item_condition(listing):
    try:
        condition = listing.find("span", class_="SECONDARY_INFO").text
        listing_condition.append(condition)
    except AttributeError:
        listing_condition.append("")


def fetch_item_shipping(listing):
    try:
        shipping = listing.find("span", class_="s-item__shipping s-item__logisticsCost").text.strip()
        listing_shipping.append(shipping)
    except AttributeError:
        listing_shipping.append("")


def is_auction(listing):
    try:
        auction = listing.find("span", class_="s-item__bids s-item__bidCount").text
        if auction is not None:
            listing_auction.append(True)
    except AttributeError:
        listing_auction.append(False)

def best_offer(listing):
    try:
        offer = listing.find("span", class_="s-item__dynamic s-item__formatBestOfferAccepted").text
        if offer is not None:
            no_best_offer.append(False)
    except AttributeError:
        no_best_offer.append(True)


for page in range(1, number_of_pages):
    url = "https://www.ebay.ca/sch/i.html?_from=R40&_nkw=new+3ds+&_sacat=0&LH_Sold=1&LH_Complete=1&Model=New%2520Nintendo%25203DS%2520LL%7CNew%2520Nintendo%25203DS%2520XL&_oaa=1&_dcat=139971&_stpos=T2Z3N7&_fcid=2&rt=nc&LH_All=1&_pgn=" + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    entries = soup.find_all("li", class_="s-item s-item__pl-on-bottom")

    for item in entries[2:]:
        fetch_item_title(item)
        fetch_item_price(item)
        fetch_item_condition(item)
        fetch_item_shipping(item)
        is_auction(item)
        best_offer(item)

df = pd.DataFrame({"Title": listing_title,
                   "Price": listing_price,
                   "Shipping": listing_shipping,
                   "Condition": listing_condition,
                   "Is Auction?": listing_auction,
                   "No Best Offer": no_best_offer})


df.to_csv("Ebay_3ds_EDA.csv",  index=False)

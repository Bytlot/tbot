import requests
from bs4 import BeautifulSoup

# http://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-us, en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', })


def get_soup(url):

    webpage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    return soup


def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id": 'productTitle'})

        # Inner NavigableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip()

        # # Printing types of values for efficient understanding
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price


def get_price(soup):

    try:
        price_whole = soup.find(
            "span", attrs={'class': "a-price-whole"}).text.strip()
        price_fraction = soup.find(
            "span", attrs={'class': "a-price-fraction"}).text.strip()
        price = price_whole + price_fraction

    except AttributeError:
        price = ""

    return price

# Function to extract Product Rating


def get_rating(soup):

    try:
        rating = soup.find(
            "i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:

        try:
            rating = soup.find(
                "span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating

# Function to extract Number of User Reviews


def get_review_count(soup):
    try:
        review_count = soup.find(
            "span", attrs={'id': 'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count

# Function to extract Availability Status


def get_availability(soup):
    try:
        soup.select('#availability .a-color-state')[0].get_text().strip()
        stock = 'Out of Stock'
    except:
        # checking if there is "Out of stock" on a second possible position
        try:
            soup.select('#availability .a-color-price')[0].get_text().strip()
            stock = 'Out of Stock'
        except:
            # if there is any error in the previous try statements, it means the product is available
            stock = 'Available'
    return stock

    # try:
    #     available = soup.find("div", attrs={'id': 'availability'})
    #     available = available.find("span").string.strip()

    # except AttributeError:
    #     available = ""

    # return available


if __name__ == '__main__':

    # Headers for request

    # The webpage URL
    URL = "https://www.amazon.com/Pampers-Training-Underwear-5t-6t-Count/dp/B01M2CZBCD/ref=sr_1_3?crid=KSTW33I9DL74&dchild=1&keywords=pampers+easy+ups+5t-6t&qid=1626787064&sprefix=pampers+ea%2Caps%2C195&sr=8-3"

    # HTTP Request

    # Soup Object containing all data
    soup = get_soup(URL)

    # Function calls to display all necessary product information
    # print("Product Title =", get_title(soup))
    print("Product Price =", get_price(soup))
    # print("Product Rating =", get_rating(soup))
    # print("Number of Product Reviews =", get_review_count(soup))
    # print("Availability =", get_availability(soup))
    # print()
    print()

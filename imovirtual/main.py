
import requests     # request information from web page

#db= MySQLdb.connect()

from bs4 import BeautifulSoup   #website to data

#api_adres = 'http://api.wunderground.com/api/7a72cf5ef1d71065/conditions/q/CA/San_Francisco.json'
#json_data = requests.get(api_adres).json()
#x=json_data['current_observation']['display_location']['zip']
#print(x)

def comprar_spider(max_pages):   #what if a hundred pages?
    nrAdsPerPage = 24        #page counter -- it changes every time it loop through a page
    while nrAdsPerPage <= max_pages:
        url = 'https://www.imovirtual.com/comprar/apartamento/?nrAdsPerPage=72&page=' + str(nrAdsPerPage)
        source_code = requests.get(url)  #connectited to web page
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)  #all the source code from the website + soup object--find all the links/titles in soup

        #find the something unique in the source code ---->> 'offer-item-title'

        #it is gonna loop thorugh all of the source code and it's gonna pick out the links eith a class of 'offer-item-title'

        for link in soup.find_all('a'):
            if link.find_all('span', {'class': 'offer-item-title'}):
                href = link.get('href')
                print(href)
                get_price(href)
                get_area(href)
                #get_single_item_data(href)
                for k in link.find_all('span', {'class': 'offer-item-title'}):
                    title = k.string
                    print(title)
                    print("\n")

        nrAdsPerPage+=24

def get_price(item_url):
    source_code = requests.get(item_url)  # connectited to web page
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for link2 in soup.find_all('div', {'class': "box-price text-right"}):
        if link2.find_all('strong', {'class': 'box-price-value no-estimates'}):
            for k in link2.find_all('strong', {'class': 'box-price-value no-estimates'}):
                title = k.string
                print(title)

    #print the links of each page
    #for link in soup.find_all('a'):
     #   href =  link.get('href')
     #   print(href)


def get_area(item_url):
    source_code = requests.get(item_url)
    plain_text= source_code.text
    soup = BeautifulSoup(plain_text)

    for link3 in soup.find_all('div',{'class': 'area-lane'}):
        for k in link3.find_all('span',{'class': 'big'}):
            print(k.string)



comprar_spider(24)




import requests, csv
from bs4 import BeautifulSoup as bs

restaurants = []

with open('restaurants.csv', mode='r') as restaurant_input:
    for line in restaurant_input:
        restaurants.append(line.strip("\n").split(","))



output = open('food_db.csv', mode='w')
output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for r in restaurants:
    print (r)
    URL = r[1]
    res=requests.get(URL)
    soup=bs(res.text,"lxml")
    items= soup.findAll('li', {"class":"menu-index-page__item"})

    for item in items:
        restaurant = r
        title = item.find('h6').getText()
        print (title, end="\t")
        price = item.find('span', {"class":"menu-index-page__item-price"}).getText()
        print (price[4:])
        # img = item.find('div', {"class":"menu-index-page__item-image"})["style"]
        # print (img, end="\t")
        output.writerow([title, price[4:], r[0], r[1], 'Deliveroo'])

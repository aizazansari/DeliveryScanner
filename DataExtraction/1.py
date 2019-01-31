import requests, csv
from bs4 import BeautifulSoup as bs

res=requests.get('https://deliveroo.ae/restaurants/abu-dhabi/saadiyat?geohash=thqew8w1j5f1')
soup=bs(res.text,"lxml")
items= soup.find('div', {"class":"RestaurantsPageLayout-8668a82aa5600d6d"}).findAll('div', {"class":"RestaurantCard-4ed7f323d018d7ae"})

restaurant_output = open('restaurants.csv', mode='w')
restaurant_output = csv.writer(restaurant_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for item in items:
    title = item.find('p', {"class":"ccl-19882374e640f487"}).getText()
    print (title)
    link = item.a["href"]
    print (link)
    restaurant_output.writerow([title, link])

import csv


with open('food_db', mode='r') as restaurant_input:
    for line in restaurant_input:
        restaurants.append(line.strip("\n").split(","))



output = open('food_db2.csv', mode='w')
output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for r in restaurants:
    URL = r[1]
    res=requests.get(URL)
    soup=bs(res.text,"lxml")
    items= soup.find('div', {"class":"rest-menu-items-wrapper"}).div.findAll(('div', {"class":"col-md-6 menu-item"}))
    
    for item in items:
    #    restaurant = r
        print()
        try:
            title = item.find('div', {"class":"menu-item-info"}).h4.getText()
            print (title, end="\t")
            price = item.find('p', {"class":"price"}).getText()
            print (price, end="\t")
            img = item.find('div', {"class":"menu-item-cover"})["style"][22:-2]
            print (img)
        except:
            pass

        output.writerow([title, price, r[0], r[1], 'Carriage', img])


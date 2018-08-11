import requests
from bs4 import BeautifulSoup
url = 'https://phillipsacademy.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=4236'
resp = requests.get(url)
html = BeautifulSoup(resp.content, 'html.parser')
#html_str = html.get_text().encode('ascii', 'ignore')
meal_period_r = html.find_all("a", class_= "menu-period")
meal_period = []
for item in meal_period_r:
    meal_period.append(item.get('href'))
links = []
start = 'https://phillipsacademy.campusdish.com'
for s in meal_period:
    links.append(start + s)
menu_item = []
for link in links:
    resp = requests.get(link)
    html = BeautifulSoup(resp.content, 'html.parser')
    menu_item_r = html.find_all("span", class_ = "menu-item-name")
    for item in menu_item_r:
        menu_item.append(item.get_text())
print(menu_item)
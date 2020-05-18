import requests
from bs4 import BeautifulSoup
import json
from openpyxl import Workbook
import datetime

list = []
dell = []
des = []
# temp = []
final = []
Result = []
count= 0
# last ={}



def Soup(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except:
        with open('exceptions.txt', 'a') as File:
            now = datetime.datetime.now()
            str = f"Could not get the url, {now}"
            File.write(str)
    return soup


def Getting_data(soup):
    count = 0
    for i in soup.find_all('div'):
        z = (i.get('class'))
        if z is not None and z[0] == "mobile-nav":
            lis = i.find_all('a')
            for j in lis:
                k = j.get('href')
                list.append(k)
    print("links found")
    # for item in list:
    response = requests.get(list[1])
    soup = BeautifulSoup(response.text, 'html.parser')
    for i in soup.find_all('div'):
        s = (i.get('class'))
        if s is not None and s[0] == 'product':
            new = i.find('a').get('href')
            dell.append(new)
    print('starting finding data')
    for u in tqdm(dell):
        res = requests.get(u)
        soup = BeautifulSoup(res.text, 'html.parser')
        for n in soup.find_all('h1'):
            x = n.get("class")
            if x is not None and x == "product-nameed entry-title":
                name = n.text
        for c in soup.find_all('div'):
            f = c.get('class')
            if f is not None and f[0] == 'product-short-desc':
                for j in c.find_all('span'):
                    desc = j.text
                    des.append(desc)
        for i in soup.find_all('span'):
            b = i.get('itemprop')
            if b is not None and b == "brand":
                brand = i.text
        for i in soup.find_all('div'):
            b = i.get('itemprop')
            if b is not None and b == "description":
                data = i.text
        count += 1

        temp = [count, des[0], des[1], des[2], des[3]]
        des.clear()
        final.append(temp)
    return final

def Excel(data):
    book = Workbook()
    sheet = book.active
    headers = ['Number', 'Screen_size', 'processor', 'graphic_processor', 'RAM']
    sheet.append(headers)
    for i in final:
        sheet.append(i)

    book.save('nikita.xlsx')


def Start(url):
    print('getting soup') 
    soup = Soup('https://www.nologygate.com/laptops')
    print("getting data")
    data = Getting_data(soup)
    print('Creating excel file')
    Excel(data)




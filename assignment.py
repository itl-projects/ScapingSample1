from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
reports =[]
titles = []
amount =[]
department= []
transaction =[]
views =[]
city = []
date =[]


def Soup():
    main =[]
    urls = []
    for a in range(1, 5):
        a *= 10
        string = "http://www.ipaidabribe.com/reports/all?page=" + str(a)
        urls.append(string)
    print(urls)
    for i in urls:
        print(i)
        response = requests.get(i)
        soup = BeautifulSoup(response.text, 'html.parser')

        for i in soup.find_all('h3'):
            z = i.get('class')
            if z is not None and z[0] == "heading-3":
                x = i.find('a').get('title')
                titles.append(x)
        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "paid-amount":
                y = i.find('span')
                amount.append(y.text)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "views":
                views.append(i.text)

        for i in soup.find_all('div'):
            z = i.get('class')
            if z is not None and z[0] == "key":
                c = i.find('a').get('title')
                city.append(c)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "transaction":
                t = i.find('a').get('title')
                transaction.append(t)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "name":
                t = i.find('a').get('title')
                department.append(t)

        for i in soup.find_all('li'):
            z = i.get('class')
            if z is not None and z[0] == "time-span":
                date.append(i.text)
        final = []
        for i in range(0, 10):
            temp = [date[i], titles[i], amount[i], department[i], transaction[i], views[i], city[i]]
            print(temp)
            final.append(temp)
            print(final)
        main.append(final)
        temp.clear()
        final.clear()
    return main

    # for i in final:
    #     if i is None:
    #         i.remove
    # print(final)
# def Pages():
#     for i in url():
#         data =


def Excel(final):
    book = Workbook()
    sheet = book.active
    headers = ['date', 'Title', 'Amount', 'Department', 'transaction','views','city',]
    sheet.append(headers)
    for i in final:
        for j in i:
            sheet.append(j)
    book.save('assignment.xlsx')

def start():
    main =[]
    print('starting')
    data1 = Soup('http://www.ipaidabribe.com/reports/all?page=#gsc.tab=0')
    main.append(data1)
    print(main)
    links = url()
    for item in links:
        soft = Soup(item)

    main.append(soft)
    soft.clear()
    print(main)





print(Soup())